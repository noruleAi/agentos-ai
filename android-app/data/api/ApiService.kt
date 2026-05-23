package com.agentos.data.api

import com.agentos.data.models.TaskResponse
import retrofit2.http.POST
import retrofit2.http.GET
import retrofit2.http.Query

interface ApiService {
    @POST("api/tasks/create")
    suspend fun createTask(@Query("prompt") prompt: String): TaskResponse

    @GET("api/memory")
    suspend fun getMemories(): List<String>

    @POST("api/memory/save")
    suspend fun saveMemory(data: Map<String, String>): Boolean
}