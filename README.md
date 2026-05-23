# 🤖 AgentOS AI - Autonomous Multimodal AI Operating System

Production-ready AI operating system combining autonomous agents, persistent memory, multimodal intelligence, and enterprise automation.

## 🎯 Features

- **Multi-Agent Orchestration**: Planner, Coding, Research, Security agents
- **Persistent Memory**: AI memory system with Redis caching
- **Real-time Streaming**: WebSocket support for live task updates
- **Secure Execution**: Docker sandboxing for code execution
- **JWT Authentication**: Secure API endpoints
- **Cross-Platform**: Android app + FastAPI backend

## 🏗️ Architecture

### Backend Stack
- **FastAPI** - Modern async web framework
- **PostgreSQL** - Persistent data storage
- **Redis** - Caching and memory management
- **Docker** - Isolated execution environment
- **Celery** - Async task queue

### Frontend Stack
- **Kotlin** - Android development
- **Jetpack Compose** - Modern UI framework
- **MVVM** - Architecture pattern
- **Hilt** - Dependency injection

## 🚀 Quick Start

### Backend Setup

```bash
cd backend
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
docker-compose up
```

Backend runs on `http://localhost:8000`
API docs available at `http://localhost:8000/docs`

### Android Setup

1. Open `android-app` in Android Studio
2. Sync Gradle dependencies
3. Update API endpoint in `build.gradle.kts`
4. Run on emulator or device

## 📚 Project Structure

```
agentos-ai/
├── backend/
│   ├── app/
│   │   ├── api/          # API routes
│   │   ├── agents/       # AI agents
│   │   ├── core/         # Config, auth, database
│   │   ├── memory/       # Memory management
│   │   ├── cache/        # Redis cache
│   │   └── websocket/    # WebSocket manager
│   ├── requirements.txt
│   ├── docker-compose.yml
│   └── .env
└── android-app/
    ├── navigation/       # App navigation
    ├── screens/          # UI screens
    ├── viewmodels/       # MVVM viewmodels
    ├── data/
    │   ├── api/          # Retrofit API
    │   ├── repository/   # Data repositories
    │   └── models/       # Data models
    └── build.gradle.kts
```

## 🔌 API Endpoints

### Tasks
- `POST /api/tasks/create` - Create and execute AI task
- `GET /api/tasks/{task_id}` - Get task status

### Memory
- `GET /api/memory` - Retrieve user memory
- `POST /api/memory/save` - Save to memory

### WebSocket
- `WS /ws/{client_id}` - Real-time streaming

## 🔐 Security Features

- JWT Authentication
- Docker sandboxing for code execution
- Encrypted storage
- CORS protection
- Environment-based configuration

## 📊 Development Roadmap

- [x] Backend API structure
- [x] Android UI foundation
- [x] Authentication system
- [x] Memory management
- [ ] Vision AI integration
- [ ] Advanced agent routing
- [ ] Self-healing system
- [ ] Billing/subscription system
- [ ] Kubernetes deployment

## 🛠️ Technologies

- FastAPI, SQLAlchemy, PostgreSQL
- Redis, Celery, Docker
- Kotlin, Jetpack Compose, Retrofit
- Python, async/await patterns

## 📝 License

MIT License

## 🤝 Contributing

Contributions welcome! Please open issues and submit PRs.
