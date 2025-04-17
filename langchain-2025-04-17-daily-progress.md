# langchain Daily Progress - 2025-04-17

## Issues
- doc: clean doc word description. (open)
- langchain: fix mypy type ignores (open)
- core: Raise `AttributeError` (not `ModuleNotFoundError`) from`__getattr__` (open)
- opensearch: create standalone langchain-opensearch package (open)
- langchain-openai: Fix openapi _resize case. (open)
- multiple: permit optional fields on multimodal content blocks (open)
- community: Fix HTTP protocol handling in AzureAISearchRetriever._build_search_url (open)
- AIMessage not allowed as structured_output (open)
- core[patch]: add retries and better messages to draw_mermaid_png (open)
- docs: update multi-modal docs (open)
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
- langchain: catch if there are only system messages in a prompt for anthropic (open)

## Pull Requests
- doc: clean doc word description. (open)
- langchain: fix mypy type ignores (open)
- core: Raise `AttributeError` (not `ModuleNotFoundError`) from`__getattr__` (open)
- opensearch: create standalone langchain-opensearch package (open)
- langchain-openai: Fix openapi _resize case. (open)
- multiple: permit optional fields on multimodal content blocks (open)
- community: Fix HTTP protocol handling in AzureAISearchRetriever._build_search_url (open)
- core[patch]: add retries and better messages to draw_mermaid_png (open)
- docs: update multi-modal docs (open)
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

## Commits
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
- infra: run old standard-tests on core releases (#30852)

On core releases, we check out the latest published package for
langchain-openai and langchain-anthropic and run their tests against the
candidate version of langchain-core.

Because these packages have a local install of langchain-tests, we also
need to check out the previous version of langchain-tests. by ccurme
- core[fix]: remove `load` from dynamic imports dict (#30849) by Sydney Runkle
- core: release 0.3.52 (#30850) by ccurme
- Fix `from langchain_core.load.load import load` import (#30843)

TL;DR: you can't optimize imports with a lazy `__getattr__` if there is
a namespace conflict with a module name and an attribute name. We should
avoid introducing conflicts like this in the future.

This PR fixes a bug introduced by my lazy imports PR:
https://github.com/langchain-ai/langchain/pull/30769.

In `langchain_core`, we have utilities for loading and dumping data.
Unfortunately, one of those utilities is a `load` function, located in
`langchain_core/load/load.py`. To make this function more visible, we
make it accessible at the top level `langchain_core.load` module via
importing the function in `langchain_core/load/__init__.py`.

So, either of these imports should work:

```py
from langchain_core.load import load
from langchain_core.load.load import load
```

As you can tell, this is already a bit confusing. You'd think that the
first import would produce the module `load`, but because of the
`__init__.py` shortcut, both produce the function `load`.

<details> More on why the lazy imports PR broke this support...

All was well, except when the absolute import was run first, see the
last snippet:

```
>>> from langchain_core.load import load
>>> load
<function load at 0x101c320c0>
```

```
>>> from langchain_core.load.load import load
>>> load
<function load at 0x1069360c0>
```

```
>>> from langchain_core.load import load
>>> load
<function load at 0x10692e0c0>
>>> from langchain_core.load.load import load
>>> load
<function load at 0x10692e0c0>
```

```
>>> from langchain_core.load.load import load
>>> load
<function load at 0x101e2e0c0>
>>> from langchain_core.load import load
>>> load
<module 'langchain_core.load.load' from '/Users/sydney_runkle/oss/langchain/libs/core/langchain_core/load/load.py'>
```

In this case, the function `load` wasn't stored in the globals cache for
the `langchain_core.load` module (by the lazy import logic), so Python
defers to a module import.

</details>

New `langchain` tongue twister 😜: we've created a problem for ourselves
because you have to load the load function from the load file in the
load module 😨. by Sydney Runkle
- core[patch]: dict chat prompt template support (#25674)

- Support passing dicts as templates to chat prompt template
- Support making *any* attribute on a message a runtime variable
- Significantly simpler than trying to update our existing prompt
template classes

```python
    template = ChatPromptTemplate(
        [
            {
                "role": "assistant",
                "content": [
                    {
                        "type": "text",
                        "text": "{text1}",
                        "cache_control": {"type": "ephemeral"},
                    },
                    {"type": "image_url", "image_url": {"path": "{local_image_path}"}},
                ],
                "name": "{name1}",
                "tool_calls": [
                    {
                        "name": "{tool_name1}",
                        "args": {"arg1": "{tool_arg1}"},
                        "id": "1",
                        "type": "tool_call",
                    }
                ],
            },
            {
                "role": "tool",
                "content": "{tool_content2}",
                "tool_call_id": "1",
                "name": "{tool_name1}",
            },
        ]
    )

```

will likely close #25514 if we like this idea and update to use this
logic

---------

Co-authored-by: Chester Curme <chester.curme@gmail.com> by Bagatur
- multiple: multi-modal content blocks (#30746)

Introduces standard content block format for images, audio, and files.

## Examples

Image from url:
```
{
    "type": "image",
    "source_type": "url",
    "url": "https://path.to.image.png",
}
```


Image, in-line data:
```
{
    "type": "image",
    "source_type": "base64",
    "data": "<base64 string>",
    "mime_type": "image/png",
}
```


PDF, in-line data:
```
{
    "type": "file",
    "source_type": "base64",
    "data": "<base64 string>",
    "mime_type": "application/pdf",
}
```


File from ID:
```
{
    "type": "file",
    "source_type": "id",
    "id": "file-abc123",
}
```


Plain-text file:
```
{
    "type": "file",
    "source_type": "text",
    "text": "foo bar",
}
``` by ccurme
- docs: fix tools_human.ipynb url 404. (#30831)

Fix the 404 pages.

Signed-off-by: zhanluxianshen <zhanluxianshen@163.com> by 湛露先生
- core: codspeed tweak to make sure it runs on master (#30845) by Sydney Runkle
- Tinkering with CodSpeed (#30824)

Fix CI to trigger benchmarks on `run-codspeed-benchmarks` label addition

Reduce scope of async benchmark to save time on CI

Waiting to merge this PR until we figure out how to use walltime on
local runners. by Sydney Runkle
- Consistent docstring indentation (#30834)

Should be 4 spaces instead of 3. by William FH
- docs: small Tableau docs update (#30827)

Description: small Tableau docs update
Issue: adds required environment variable
Dependencies: tableau-langchain

---------

Co-authored-by: Joe Constantino <joe.constantino@joecons-ltm6v86.internal.salesforce.com> by Joey Constantino
- openai[patch]: update imports in test (#30828)

Quick fix to unblock CI, will need to address in core separately. by ccurme
- core[lint]: fix issue with unused ignore in `__init__.py` files (#30825)

Fixing a race condition between
https://github.com/langchain-ai/langchain/pull/30769 and
https://github.com/langchain-ai/langchain/pull/30737 by Sydney Runkle
