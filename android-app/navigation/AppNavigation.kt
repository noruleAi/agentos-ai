package com.agentos.ui.navigation

import androidx.compose.runtime.Composable
import androidx.navigation.NavHostController
import androidx.navigation.compose.NavHost
import androidx.navigation.compose.composable
import com.agentos.ui.screens.DashboardScreen
import com.agentos.ui.screens.ChatScreen
import com.agentos.ui.screens.SettingsScreen
import com.agentos.ui.screens.MemoryScreen

@Composable
fun AppNavigation(navController: NavHostController) {
    NavHost(
        navController = navController,
        startDestination = "dashboard"
    ) {
        composable("dashboard") {
            DashboardScreen(navController = navController)
        }

        composable("chat") {
            ChatScreen(navController = navController)
        }

        composable("memory") {
            MemoryScreen(navController = navController)
        }

        composable("settings") {
            SettingsScreen(navController = navController)
        }
    }
}