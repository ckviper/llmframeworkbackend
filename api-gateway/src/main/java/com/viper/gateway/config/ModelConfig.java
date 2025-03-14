package com.viper.gateway.config;

import lombok.Builder;
import lombok.Getter;
import lombok.Setter;
import lombok.extern.jackson.Jacksonized;

@Getter
@Setter
@Jacksonized
@Builder(toBuilder = true)
public class ModelConfig {
    private String name;
    private String version;
    private String modelId;
    private String description;
    private String endpoint;
    private String host;
}
