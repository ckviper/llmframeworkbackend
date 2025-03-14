package project.plugins

import org.gradle.api.Plugin
import org.gradle.api.Project
import org.gradle.api.artifacts.Configuration
import org.gradle.api.tasks.testing.Test
import org.gradle.jvm.toolchain.JavaLanguageVersion
import org.gradle.kotlin.dsl.assign
import org.gradle.kotlin.dsl.dependencies
import org.gradle.kotlin.dsl.named
import org.gradle.kotlin.dsl.withType
import org.jetbrains.kotlin.gradle.utils.extendsFrom
import project.extensions.annotationProcessor
import project.extensions.implementation
import project.extensions.libs
import project.extensions.testImplementation

class ViperMicroservicePlugin : Plugin<Project> {
    override fun apply(target: Project) = with(target) {
        with(pluginManager) {
            this.apply("org.gradle.java")
            this.apply(libs.plugins.spring.boot.get().pluginId)
            this.apply(libs.plugins.spring.dependency.management.get().pluginId)
        }

        configurations.named<Configuration>("compileOnly")
            .extendsFrom(configurations.named<Configuration>("annotationProcessor"))

        dependencies {
            implementation(libs.spring.boot.starter.web)
            implementation(libs.spring.boot.starter.actuator)
            implementation(libs.spring.boot.starter.data.jpa)
            implementation(libs.spring.boot.starter.validation)
            implementation(libs.spring.boot.starter.websocket)
            implementation(libs.spring.kafka)
            implementation(libs.lombok)
            implementation(libs.mapstruct)
            implementation(libs.mapstruct.processor)
            annotationProcessor(libs.lombok)
            annotationProcessor(libs.mapstruct.processor)
            annotationProcessor(libs.spring.boot.configuration.processor)
            testImplementation(libs.spring.boot.starter.test)
        }

        tasks.withType<Test> {
            useJUnitPlatform()
        }

        (this as org.gradle.api.plugins.ExtensionAware).extensions.configure<org.gradle.api.plugins.JavaPluginExtension>("java") {
            toolchain {
                languageVersion = JavaLanguageVersion.of(17)
            }
        }
    }
}