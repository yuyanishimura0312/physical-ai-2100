Reading additional input from stdin...
2026-05-13T13:42:15.383866Z ERROR codex_models_manager::manager: failed to refresh available models: unexpected status 401 Unauthorized: Your authentication token has been invalidated. Please try signing in again., url: https://chatgpt.com/backend-api/codex/models?client_version=0.128.0, cf-ray: 9fb215d92a8abf9f-NRT, request id: 3f4d9881-0592-4591-8589-6ba63aabc218, auth error: 401, auth error code: token_invalidated
2026-05-13T13:42:16.102393Z ERROR codex_models_manager::manager: failed to refresh available models: unexpected status 401 Unauthorized: Your authentication token has been invalidated. Please try signing in again., url: https://chatgpt.com/backend-api/codex/models?client_version=0.128.0, cf-ray: 9fb215ddbc9111d3-NRT, request id: 4b788fa3-8324-4150-859c-bf18f6971ca6, auth error: 401, auth error code: token_invalidated
OpenAI Codex v0.128.0 (research preview)
--------
workdir: /Users/nishimura+/projects/research/physical-ai-2100/phase1_papers
model: gpt-5.5
provider: openai
approval: never
sandbox: workspace-write [workdir, /tmp, $TMPDIR, /Users/nishimura+/.codex/memories]
reasoning effort: none
reasoning summaries: none
session id: 019e2192-e72b-7c41-92df-278757f6ea6b
--------
user
あなたは学術論文収集の専門家です。Web検索（arXiv, Google Scholar, Semantic Scholar, OpenReview等）を駆使して、以下のテーマの主要な学術論文を50件以上、極めて精密に抽出してください。

【出力形式（Markdown）】
各論文を以下の形式で：
## [番号]. [論文タイトル]
- 著者: 主要著者3-5名
- 発表年: YYYY
- 会議/ジャーナル: 例 NeurIPS 2023, Science Robotics
- 被引用数: 概数
- arXiv/DOI: URL or ID
- 核心貢献（3-5行）: 何を提案し、何を実証したか
- PHAI-DB分類: stream (AI/Robotics/Bio/Materials/Cognitive) / phase (A〜G) / 関連concept群

【絶対条件】
- 実在する論文のみ。ハルシネーション禁止。
- 50件以上を強く目指す。
- 出力はファイル冒頭にタイトル「# Physical AI Papers — [テーマ]」を含むこと。

【テーマ】

Embodied AI / Vision-Language-Action Foundation Models（VLA基盤モデル）。RT-1, RT-2, OpenVLA, Octo, RT-X, RoboCat, PaLM-E, Voxposer 等。CoRL/ICRA/RSS/NeurIPS/ICML 2020-2026の主要論文を網羅的に。
2026-05-13T13:42:17.283405Z ERROR rmcp::transport::worker: worker quit with fatal: Transport channel closed, when UnexpectedContentType(Some("text/plain; body: {\n  \"error\": {\n    \"message\": \"Your authentication token has been invalidated. Please try signing in again.\",\n    \"type\": \"invalid_request_error\",\n    \"code\": \"token_invalidated\",\n    \"param\": null\n  },\n  \"status\": 401\n}"))
2026-05-13T13:42:18.050665Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:18.729914Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:19.773266Z ERROR codex_login::auth::manager: Failed to refresh token: 401 Unauthorized: {
  "error": {
    "message": "Your refresh token has already been used to generate a new access token. Please try signing in again.",
    "type": "invalid_request_error",
    "param": null,
    "code": "refresh_token_reused"
  }
}
2026-05-13T13:42:21.012874Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
2026-05-13T13:42:25.905542Z ERROR codex_api::endpoint::responses_websocket: failed to connect to websocket: HTTP error: 401 Unauthorized, url: wss://chatgpt.com/backend-api/codex/responses
ERROR: Your access token could not be refreshed because your refresh token was already used. Please log out and sign in again.
ERROR: Your access token could not be refreshed because your refresh token was already used. Please log out and sign in again.
