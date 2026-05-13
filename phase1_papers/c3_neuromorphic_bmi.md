Reading additional input from stdin...
2026-05-13T13:42:15.272915Z ERROR codex_models_manager::manager: failed to refresh available models: unexpected status 401 Unauthorized: Your authentication token has been invalidated. Please try signing in again., url: https://chatgpt.com/backend-api/codex/models?client_version=0.128.0, cf-ray: 9fb215d7aa022627-NRT, request id: cd0efdd3-a96e-45fd-8a84-c166b5865174, auth error: 401, auth error code: token_invalidated
2026-05-13T13:42:16.101299Z ERROR codex_models_manager::manager: failed to refresh available models: unexpected status 401 Unauthorized: Your authentication token has been invalidated. Please try signing in again., url: https://chatgpt.com/backend-api/codex/models?client_version=0.128.0, cf-ray: 9fb215dd6bf1eb98-NRT, request id: f03183cb-8e5e-4cc9-8247-83332118b528, auth error: 401, auth error code: token_invalidated
OpenAI Codex v0.128.0 (research preview)
--------
workdir: /Users/nishimura+/projects/research/physical-ai-2100/phase1_papers
model: gpt-5.5
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR, /Users/nishimura+/.codex/memories]
reasoning effort: none
reasoning summaries: none
session id: 019e2192-e72b-7ab1-9b74-2615fe568abc
--------
user


Neuromorphic Computing / Brain-Machine Interface / Embodied Cognition。神経模倣チップ（Loihi, TrueNorth, SpiNNaker）、Spiking Neural Networks、BCI（Neuralink, Synchron）、Active Inference、Predictive Coding。Nature, Neuron, IEEE Trans 2015-2026の主要論文を網羅的に。
2026-05-13T13:42:16.873074Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when UnexpectedContentType(Some("text/plain; body: {\n  \"error\": {\n    \"message\": \"Your authentication token has been invalidated. Please try signing in again.\",\n    \"type\": \"invalid_request_error\",\n    \"code\": \"token_invalidated\",\n    \"param\": null\n  },\n  \"status\": 401\n}"))
2026-05-13T13:42:17.729003Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:18.528494Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:19.794498Z ERROR codex_login::auth::manager: Failed to refresh token: 401 Unauthorized: {
  "error": {
    "message": "Your refresh token has already been used to generate a new access token. Please try signing in again.",
    "type": "invalid_request_error",
    "param": null,
    "code": "refresh_token_reused"
  }
}
2026-05-13T13:42:26.217612Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:26.919432Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
ERROR: Your access token could not be refreshed because your refresh token was already used. Please log out and sign in again.
ERROR: Your access token could not be refreshed because your refresh token was already used. Please log out and sign in again.
