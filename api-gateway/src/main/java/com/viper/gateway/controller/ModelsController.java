package com.viper.gateway.controller;

import com.viper.gateway.config.ModelConfig;
import com.viper.gateway.config.ModelsConfig;
import lombok.RequiredArgsConstructor;
import org.springframework.web.bind.annotation.GetMapping;
import org.springframework.web.bind.annotation.PathVariable;
import org.springframework.web.bind.annotation.RestController;

import java.util.List;

@RestController
@RequiredArgsConstructor
public class ModelsController {
    private final ModelsConfig modelsConfig;

    @GetMapping("v1/models")
    public List<ModelConfig> getModelsConfig() {
        return modelsConfig.getModels();
    }

    @GetMapping("v1/models/{modelId}")
    public ModelConfig getModelConfig(@PathVariable String modelId) {
        for (ModelConfig modelConfig : modelsConfig.getModels()) {
            if (modelConfig.getName().equals(modelId)) {
                return modelConfig;
            }
        }
        return null;
    }
}
