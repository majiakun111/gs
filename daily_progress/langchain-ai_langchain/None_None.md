# langchain Daily Progress - None to None

## Issues
- core: Fix some private member accesses (open)
- Tool Call Fails: Constructs Invalid Arguments When The Function Accepts Arguments of Type Dictionary (open)
- Support of openai reasoning summary streaming (open)
- text-splitters: Set strict mypy rules (open)
- community: fix cost calculations for 4.1 and o4 in OpenAI callback (open)
- OpenAICallbackHandler does not have cost information for Open AI 4.1 and o4 models (open)
- Deprecate HanaDB, HanaTranslator and update example notebook to use new implementation  (open)
- opensearch: create standalone langchain-opensearch package (open)
- langchain-openai: Fix openapi _resize case. (open)
- community: Fix HTTP protocol handling in AzureAISearchRetriever._build_search_url (open)
- AIMessage not allowed as structured_output (open)
- `langchain-chroma`: Query filters are extremely restrictive (by type), is this by design?? (open)
- community: add gpt-4.1 and gpt-4.5-preview model pricing and name handling (open)
- community: Remove no-untyped-def escapes (open)
- langchain_openai: clean duplicate code for openai embedding. (open)
- Bug: llm.ainvoke is traced different from llm.invoke (won't be traced) (open)
- Fix async indexing issue (open)
- langchain: return attachments in _get_response (open)
- _get_response from base.py does not return generated file id when running as an agent (open)
- [community] Propose PDFRouterParser and Loader (open)
- community: Add deprecation decorator to SingleStore community integrations (open)
- AzureCosmosDBNoSqlVectorSearch custom text_key, metadata_key, embedding_key key error (open)
- [community] Propose some @deprecated APIs for PDF (open)
- docs: Register langchain-singlestore integration (open)
- AWS OSS Doc ID and Filter nor working (open)
- ChatTongyi has the with_stuctured_output method, but it is always None (open)
- Scope Error while trying to use Anthropic Model with GoogleVertex library. (open)
- Remote malicious email injection which leads to control of the agent and forward the user's email (open)
- community: Strip URLs from sitemap. (open)
- SitemapLoader URLs are not properly strippe (open)

## Pull Requests
- core: Fix some private member accesses (open)
- Support of openai reasoning summary streaming (open)
- text-splitters: Set strict mypy rules (open)
- community: fix cost calculations for 4.1 and o4 in OpenAI callback (open)
- Deprecate HanaDB, HanaTranslator and update example notebook to use new implementation  (open)
- opensearch: create standalone langchain-opensearch package (open)
- langchain-openai: Fix openapi _resize case. (open)
- community: Fix HTTP protocol handling in AzureAISearchRetriever._build_search_url (open)
- community: add gpt-4.1 and gpt-4.5-preview model pricing and name handling (open)
- community: Remove no-untyped-def escapes (open)
- langchain_openai: clean duplicate code for openai embedding. (open)
- Fix async indexing issue (open)
- langchain: return attachments in _get_response (open)
- [community] Propose PDFRouterParser and Loader (open)
- community: Add deprecation decorator to SingleStore community integrations (open)
- [community] Propose some @deprecated APIs for PDF (open)
- docs: Register langchain-singlestore integration (open)
- community: Strip URLs from sitemap. (open)
- langchain: catch if there are only system messages in a prompt for anthropic (open)
- Feature/persian text processing (open)
- community: add mypy warn_unused_ignores rule (open)
- community: have ChatLlamaCpp handle "auto" and "any" for tool_choice (open)
- partners: ChatAnthropic supports urls (open)
- langchain: improve performance split_list_of_docs (open)
- Removing `dereference_refs` from `_convert_json_schema_to_openai_function` (open)
- langchain-openai: support custom fallback content for tool-only messages (open)
- Improvements to `ChatPerplexity` Integration  (open)
- core: Cleanup Pydantic models and handle deprecation warnings (open)
- Add Compass Labs toolkits to langchain docs (open)
- community: add ChatLLM7 integration (open)

## Commits
- langchain[lint]: fix mypy type ignores (#30894)

* Remove unused ignores
* Add type ignore codes
* Add mypy rule `warn_unused_ignores`
* Add ruff rule PGH003

NB: some `type: ignore[unused-ignore]` are added because the ignores are
needed when `extended_testing_deps.txt` deps are installed. by Christophe Bornet
- docs: update multi-modal docs (#30880)

Co-authored-by: Sydney Runkle <54324534+sydney-runkle@users.noreply.github.com> by ccurme
- core: release 0.3.54 (#30911) by Sydney Runkle
- core[patch]: add retries and better messages to draw_mermaid_png (#30881) by Vadym Barda
- core[patch]: Raise `AttributeError` (instead of `ModuleNotFoundError`) in custom `__getattr__` (#30905)

Follow up to https://github.com/langchain-ai/langchain/pull/30769,
fixing the regression reported
[here](https://github.com/langchain-ai/langchain/pull/30769#issuecomment-2807483610),
thanks @krassowski for the report!

Fix inspired by https://github.com/PrefectHQ/prefect/pull/16172/files

Other changes:
* Using tuples for `__all__`, except in `output_parsers` bc of a list
namespace conflict
* Using a helper function for imports due to repeated logic across
`__init__.py` files becoming hard to maintain.

Co-authored-by: Michał Krassowski < krassowski 5832902+krassowski@users.noreply.github.com>" by Sydney Runkle
- openai: release 0.3.14 (#30908) by ccurme
- anthropic: release 0.3.12 (#30907) by ccurme
- standard-tests: release 0.3.19 (#30906) by ccurme
- standard-tests, openai[patch]: add support standard audio inputs (#30904) by ccurme
- core: release 0.3.53 (#30901) by ccurme
- multiple: permit optional fields on multimodal content blocks (#30887)

Instead of stuffing provider-specific fields in `metadata`, they can go
directly on the content block. by ccurme
- doc: clean doc word description. (#30895)

Signed-off-by: zhanluxianshen <zhanluxianshen@163.com> by 湛露先生
- partners:  bug fix check_imports.py exit code. (#30897)

Signed-off-by: zhanluxianshen <zhanluxianshen@163.com> by 湛露先生
- docs: update Bedrock chat model page (#30883)

- document prompt caching
- feature ChatBedrockConverse throughout by ccurme
- docs: minor clean up in ChatOpenAI docs (#30884) by ccurme
- docs: document OpenAI reasoning summaries (#30882) by ccurme
- core: Removing unnecessary `pydantic` core schema rebuilds (#30848)

We only need to rebuild model schemas if type annotation information
isn't available during declaration - that shouldn't be the case for
these types corrected here.

Need to do more thorough testing to make sure these structures have
complete schemas, but hopefully this boosts startup / import time. by Sydney Runkle
- Galaxia integration (#30792)

- [ ] **PR title**: "docs: adding Smabbler's Galaxia integration"

- [ ] **PR message**:  **Twitter handle:** @Galaxia_graph

I'm adding docs here + added the package to the packages.yml. I didn't
add a unit test, because this integration is just a thin wrapper on top
of our API. There isn't much left to test if you mock it away.

---------

Co-authored-by: Chester Curme <chester.curme@gmail.com> by rrozanski-smabbler
- ollama: release 0.3.2 (#30865) by ccurme
- docs: enforce newlines when signature exceeds char threshold (#30866)

Below is an example of the single line vs new multiline approach.

Before this PR:

<img width="831" alt="Screenshot 2025-04-15 at 8 56 26 PM"
src="https://github.com/user-attachments/assets/0c0277bd-2441-4b22-a536-e16984fd91b7"
/>

After this PR:

<img width="829" alt="Screenshot 2025-04-15 at 8 56 13 PM"
src="https://github.com/user-attachments/assets/e16bfe38-bb17-48ba-a642-e8ff6b48e841"
/> by Sydney Runkle
- langchain: infer Perplexity provider for sonar model prefix (#30861)

**Description:** This PR adds provider inference logic to
`init_chat_model` for Perplexity models that use the "sonar..." prefix
(`sonar`, `sonar-pro`, `sonar-reasoning`, `sonar-reasoning-pro` or
`sonar-deep-research`).

This allows users to initialize these models by simply passing the model
name, without needing to explicitly set `model_provider="perplexity"`.

The docstring for `init_chat_model` has also been updated to reflect
this new inference rule. by milosz-l
- ollama[patch]: support standard image format (#30864)

Following https://github.com/langchain-ai/langchain/pull/30746 by ccurme
- ollama[patch]: fix generation info (#30863)

https://github.com/langchain-ai/langchain/pull/30778 (not released)
broke all invocation modes of ChatOllama (intent was to remove
`"message"` from `generation_info`, but we turned `generation_info` into
`stream_resp["message"]`), resulting in validation errors. by ccurme
- chroma: release 0.2.3 (#30860) by Sydney Runkle
- perplexity: release 0.1.1 (#30859) by ccurme
- openai: release 0.3.13 (#30858) by ccurme
- anthropic: release 0.3.11 (#30857) by ccurme
- core[fix]: Fix `__dir__` in `__init__.py` for `output_parsers` module (#30856)

We have a `list.py` file which causes a namespace conflict with `list`
from stdlib, unfortunately.

`__all__` is already a list, so no need to coerce. by Sydney Runkle
- core: Remove some noqa (#30855) by Christophe Bornet
- standard-tests: release 0.3.18 (#30854) by ccurme
