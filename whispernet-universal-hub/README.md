
# WhisperNet: Universal Communication Hub Starter

This starter contains all 5 microservices for the first Mega Microservice (Universal Communication Hub):
1. Cross-Platform Messaging
2. Smart AI Inbox
3. One-Click Reply
4. Voice-to-Everything
5. Multilingual Auto-Translate

## Run Locally

### Using Docker Compose
docker compose up --build

- API Gateway: http://localhost:8000
- Cross-Platform Messaging: http://localhost:8010
- Smart AI Inbox: http://localhost:8011
- One-Click Reply: http://localhost:8012
- Voice-to-Everything: http://localhost:8013
- Multilingual Translate: http://localhost:8014

### Test Endpoints via Gateway
curl http://localhost:8000/health
curl http://localhost:8000/messages/inbox
curl -X POST http://localhost:8000/messages/send -H "Content-Type: application/json" -d '{"text":"Hello"}'
curl http://localhost:8000/inbox/summary
curl -X POST http://localhost:8000/reply -H "Content-Type: application/json" -d '{"message":"Hi"}'
curl -X POST http://localhost:8000/voice -H "Content-Type: application/json" -d '{"audio":"dummy"}'
curl -X POST http://localhost:8000/translate -H "Content-Type: application/json" -d '{"text":"Hello"}'
