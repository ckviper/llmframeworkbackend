package project.extensions

import org.gradle.kotlin.dsl.DependencyHandlerScope

internal fun DependencyHandlerScope.implementation(name: Any) {
    add("implementation", name)
}

internal fun DependencyHandlerScope.compileOnly(name: Any) {
    add("compileOnly", name)
}

internal fun DependencyHandlerScope.annotationProcessor(name: Any) {
    add("annotationProcessor", name)
}

internal fun DependencyHandlerScope.api(name: Any) {
    add("api", name)
}

internal fun DependencyHandlerScope.ksp(name: Any) {
    add("ksp", name)
}

internal fun DependencyHandlerScope.kapt(name: Any) {
    add("kapt", name)
}

internal fun DependencyHandlerScope.debugImplementation(name: Any) {
    add("debugImplementation", name)
}

internal fun DependencyHandlerScope.testImplementation(name: Any) {
    add("testImplementation", name)
}