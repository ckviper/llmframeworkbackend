plugins {
    `kotlin-dsl`
}

repositories {
    mavenCentral()
}

dependencies {
    implementation(gradleApi())
    implementation(files(libs.javaClass.superclass.protectionDomain.codeSource.location))
    implementation(libs.kotlin.gradlePlugin)
    implementation(libs.openapi.generator.gradlePlugin)
}

gradlePlugin{
    plugins {
        register("viperMicroservicePlugin") {
            id = libs.plugins.viper.microservice.get().pluginId
            implementationClass = "project.plugins.ViperMicroservicePlugin"
        }
    }
}
