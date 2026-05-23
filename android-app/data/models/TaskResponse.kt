package com.agentos.data.models

data class TaskResponse(
    val task_id: String,
    val prompt: String,
    val result: String,
    val status: String
)