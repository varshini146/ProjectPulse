# ProjectPulse

> AI project memory that remembers why your team made decisions.

ProjectPulse is an AI-powered project memory agent for development teams. It helps teams preserve decisions, bugs, fixes, and changing requirements so important project context does not get lost over time.

Instead of only answering questions about the current project state, ProjectPulse uses persistent memory to recall relevant historical context.

## Demo Scenario: SmartShield

The demo uses a fictional phishing-detection project called SmartShield.

Example project history:

1. SmartShield initially chose SQLite because it was a small prototype and the team wanted to keep development simple.
2. Later, the project received a requirement to support 50,000 users.
3. ProjectPulse can recall both events and surface the historical context behind the original database decision.

This demonstrates how project memory can help teams revisit older assumptions when requirements change.

## How Hindsight Is Used

ProjectPulse uses **Hindsight** as its persistent memory layer.

- **RETAIN** stores project decisions, bugs, fixes, and requirements.
- **RECALL** retrieves relevant historical memories when a team member asks a question.
- Memory remains available across separate interactions rather than existing only inside the current conversation.

Hindsight is therefore a core part of the application's behavior, not just an external API added to the project.

Hindsight:
https://github.com/vectorize-io/hindsight

## Architecture

```text
User
  |
  v
ProjectPulse Web UI
  |
  v
Flask API
  |
  +------> Hindsight
  |          |
  |          +--> RETAIN project memories
  |          |
  |          +--> RECALL relevant memories
  |
  +------> Ollama / Llama 3.2