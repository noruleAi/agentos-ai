package com.agentos.data.repository

import com.agentos.data.api.ApiService
import javax.inject.Inject

class MemoryRepository @Inject constructor(
    private val apiService: ApiService
) {
    suspend fun getMemories() = apiService.getMemories()

    suspend fun saveMemory(data: Map<String, String>) = apiService.saveMemory(data)
}