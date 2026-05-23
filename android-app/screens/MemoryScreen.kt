package com.agentos.ui.screens

import androidx.compose.foundation.layout.*
import androidx.compose.foundation.lazy.LazyColumn
import androidx.compose.material.icons.Icons
import androidx.compose.material.icons.filled.ArrowBack
import androidx.compose.material3.*
import androidx.compose.runtime.*
import androidx.compose.ui.Modifier
import androidx.compose.ui.unit.dp
import androidx.hilt.navigation.compose.hiltViewModel
import androidx.navigation.NavController
import com.agentos.ui.viewmodels.MemoryViewModel

@Composable
fun MemoryScreen(
    navController: NavController,
    viewModel: MemoryViewModel = hiltViewModel()
) {
    val memories by viewModel.memories.collectAsState()

    Scaffold(
        topBar = {
            TopAppBar(
                title = { Text("AI Memory") },
                navigationIcon = {
                    IconButton(onClick = { navController.popBackStack() }) {
                        Icon(Icons.Filled.ArrowBack, contentDescription = "Back")
                    }
                }
            )
        }
    ) { paddingValues ->
        LazyColumn(
            modifier = Modifier
                .fillMaxSize()
                .padding(paddingValues)
                .padding(16.dp),
            verticalArrangement = Arrangement.spacedBy(12.dp)
        ) {
            items(memories.size) { index ->
                MemoryCard(memories[index])
            }
        }
    }
}

@Composable
fun MemoryCard(memory: String) {
    Card(
        modifier = Modifier.fillMaxWidth()
    ) {
        Text(
            text = memory,
            modifier = Modifier.padding(16.dp)
        )
    }
}