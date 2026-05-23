package com.agentos.data.repository

import com.agentos.data.api.ApiService
import javax.inject.Inject

class TaskRepository @Inject constructor(
    private val apiService: ApiService
) {
    suspend fun createTask(prompt: String) = apiService.createTask(prompt)
}