package com.agentos.ui.viewmodels

import androidx.lifecycle.ViewModel
import androidx.lifecycle.viewModelScope
import com.agentos.data.repository.MemoryRepository
import dagger.hilt.android.lifecycle.HiltViewModel
import kotlinx.coroutines.flow.MutableStateFlow
import kotlinx.coroutines.flow.StateFlow
import kotlinx.coroutines.launch
import javax.inject.Inject

@HiltViewModel
class MemoryViewModel @Inject constructor(
    private val repository: MemoryRepository
) : ViewModel() {
    private val _memories = MutableStateFlow(listOf<String>())
    val memories: StateFlow<List<String>> = _memories

    init {
        loadMemories()
    }

    private fun loadMemories() {
        viewModelScope.launch {
            val data = repository.getMemories()
            _memories.value = data
        }
    }
}