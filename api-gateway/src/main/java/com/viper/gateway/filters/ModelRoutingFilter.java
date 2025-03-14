package com.viper.gateway.filters;

import com.viper.gateway.config.ModelConfig;
import com.viper.gateway.config.ModelsConfig;
import org.springframework.beans.factory.annotation.Autowired;
import org.springframework.cloud.gateway.filter.GatewayFilter;
import org.springframework.cloud.gateway.filter.factory.AbstractGatewayFilterFactory;
import org.springframework.http.HttpStatus;
import org.springframework.http.server.reactive.ServerHttpRequest;
import org.springframework.stereotype.Component;
import reactor.core.publisher.Mono;

import java.net.URI;

@Component
public class ModelRoutingFilter extends AbstractGatewayFilterFactory<ModelRoutingFilter.Config> {
    @Autowired
    private ModelsConfig modelsConfig;

    public ModelRoutingFilter() {
        super(Config.class);
    }

    @Override
    public GatewayFilter apply(Config config) {
        return (exchange, chain) -> {
            String modelId = exchange.getRequest().getQueryParams().getFirst("modelId");
            String path = exchange.getRequest().getPath().value();
            ModelConfig model = modelsConfig.getModels().stream().filter(r -> r.getModelId().equals(modelId)).findFirst().orElse(null);

            String endpoint;
            if (path.contains("chat/completions")) {
                endpoint = "chat/completions";
            } else if (path.contains("completions")) {
                endpoint = "completions";
            } else {
                exchange.getResponse().setStatusCode(HttpStatus.BAD_REQUEST);
                return exchange.getResponse().writeWith(Mono.just(exchange.getResponse()
                        .bufferFactory().wrap("Invalid path".getBytes())));
            }

            String newUri = "http://localhost:" + model.getHost() + "/" + endpoint;
            ServerHttpRequest modifiedRequest = exchange.getRequest().mutate().uri(URI.create(newUri)).build();
            return chain.filter(exchange.mutate().request(modifiedRequest).build());
        };
    }

    public static class Config {
    }
}