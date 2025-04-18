# axios Daily Progress - None to None

## Issues
- onDownloadProgress occurred after request solved (open)
- Timeouts in React Native when app is in background state (open)
- Updated README to correct description of keepAlive option (open)
- Improve fetchOptions type for better autocomplete, type safety, and Next.js compatibility (open)
- Improve fetchOptions type definition for better autocomplete, type safety, Next.js extensions (open)
- Improved fetchOptions interface (open)
- fix(interceptor): correct return type in JSDoc (open)
- Enable multiple baseURLs for the same Axios instance (open)
- Post data with Credentials and set header (open)
- chore(deps-dev): bump tar-fs from 2.1.1 to 2.1.2 (open)
- failed to make bytecode (open)
- Clarify /dist output file type (open)
- fix(types): no auto complete for adapters (open)
- bug: no autocomplete in adapter (open)
- 关于 axios 的鸿蒙化适配提案 (open)
- Omitting Content-Type Header on Android results in Network Error (open)
- Laptop UI navbar issue (open)
- Axios Instance Documentation can do with some elaboration, as some functionality is left to be assumed (open)
- chore(deps-dev): bump rollup from 2.79.1 to 2.79.2 (open)
- chore(deps-dev): bump elliptic from 6.6.0 to 6.6.1 (open)
- Fix/canceled error cyclic reference (open)
- chore(deps-dev): bump browserify-sign from 4.2.1 to 4.2.3 (open)
- `JSON.stringify` overflows the stack when called on a `CanceledError` (open)
- feat(types): Allow the Params property to be typed, instead of any (open)
- Axios Class Construction config types question (open)
- fix: react native package exports support (open)
- When axios request sets maxRedirects=0 and encounters an unresponsive website, it will not execute further. (open)
- Bug: Axios version >= 1.7.0 Streaming Chunk Parsing Issue in Safari and Firefox (open)
- feat: implement zstd decompression for http adapter (open)
- Posting FormData payload with file does not receive response with Node >= 20.13.0 (open)

## Pull Requests
- Updated README to correct description of keepAlive option (open)
- Improve fetchOptions type for better autocomplete, type safety, and Next.js compatibility (open)
- Improved fetchOptions interface (open)
- fix(interceptor): correct return type in JSDoc (open)
- chore(deps-dev): bump tar-fs from 2.1.1 to 2.1.2 (open)
- fix(types): no auto complete for adapters (open)
- chore(deps-dev): bump rollup from 2.79.1 to 2.79.2 (open)
- chore(deps-dev): bump elliptic from 6.6.0 to 6.6.1 (open)
- Fix/canceled error cyclic reference (open)
- chore(deps-dev): bump browserify-sign from 4.2.1 to 4.2.3 (open)
- feat(types): Allow the Params property to be typed, instead of any (open)
- fix: react native package exports support (open)
- feat: implement zstd decompression for http adapter (open)
- Include custom response headers (open)
- feat: use a Map instead of Array to remove items when using eject (open)
- fix: empty window location in certain environments (open)
- feat: added JSDoc strings to some properties in the type declaration files to improve the user experience (open)
- [fix] Loud comment to ensure comments are preserved in the minified file (open)
- supports cloudflare worker (open)
- Update ECOSYSTEM.md (open)
- fix(types): change params type in AxiosRequestConfig (open)
- fix(TypeScript): Fix `AxiosHeaders` types (open)
- fix(types): normalize response headers to lowercase in TypeScript types (open)
- fix(requestConfig): support URL object in request handling (open)
- fix(requestConfigType): correct AxiosRequestConfig type handling (open)
- fix(http): send minimal end multipart boundary (open)
- Prioritize request-level Authorization in headers merging (open)
- Add URL Sanitization (open)
- #6625 Multiple headers handling (open)
- fix: multiple issues fixed that were found with audit (open)

## Commits
- fix(core): fix the Axios constructor implementation to treat the config argument as optional; (#6881) by Dmitriy Mozgovoy
- fix(fetch): fixed ERR_NETWORK mapping for Safari browsers; (#6767) by Dmitriy Mozgovoy
- fix(headers): fix `getSetCookie` by using 'get' method for caseless access; (#6874) by Dmitriy Mozgovoy
- fix(headers): allow iterable objects to be a data source for the set method; (#6873) by Dmitriy Mozgovoy
- chore(sponsor): update sponsor block (#6864)

Co-authored-by: DigitalBrainJS <12586868+DigitalBrainJS@users.noreply.github.com> by github-actions[bot]
- chore: update sponsors by Jay
- chore(types): move AxiosStatic#create to AxiosInstance#create (#5096)

* Add the bad test case.

* Fix and pass the test

* Update index.d.cts

---------

Co-authored-by: Jay <jasonsaayman@gmail.com> by George Cheng
- chore: create SECURITY.md by Jay
- feat(AxiosHeaders): add getSetCookie method to retrieve set-cookie headers values (#5707)

* feat(AxiosHeaders): add getSetCookie method to retrieve set-cookie header values

* refactor(AxiosHeaders.js): use logical OR instead of nullish coalescing operator in getSetCookie method

---------

Co-authored-by: Willian Agostini <willian.agostini@gmail.com.br>
Co-authored-by: Jay <jasonsaayman@gmail.com> by Willian Agostini
- chore(sponsor): update sponsor block (#6834)

Co-authored-by: DigitalBrainJS <12586868+DigitalBrainJS@users.noreply.github.com> by github-actions[bot]
- chore(release): v1.8.4 (#6844)

Co-authored-by: jasonsaayman <4814473+jasonsaayman@users.noreply.github.com> by github-actions[bot]
- fix(buildFullPath): handle `allowAbsoluteUrls: false` without `baseURL` (#6833)

Co-authored-by: Jay <jasonsaayman@gmail.com> by Marc Hassan
- chore(deps): bump tj-actions/changed-files in the github-actions group (#6838)

Bumps the github-actions group with 1 update: [tj-actions/changed-files](https://github.com/tj-actions/changed-files).


Updates `tj-actions/changed-files` from 45 to 46
- [Release notes](https://github.com/tj-actions/changed-files/releases)
- [Changelog](https://github.com/tj-actions/changed-files/blob/main/HISTORY.md)
- [Commits](https://github.com/tj-actions/changed-files/compare/v45...v46)

---
updated-dependencies:
- dependency-name: tj-actions/changed-files
  dependency-type: direct:production
  update-type: version-update:semver-major
  dependency-group: github-actions
...

Signed-off-by: dependabot[bot] <support@github.com>
Co-authored-by: dependabot[bot] <49699333+dependabot[bot]@users.noreply.github.com> by dependabot[bot]
- chore(release): v1.8.3 (#6819)

Co-authored-by: jasonsaayman <4814473+jasonsaayman@users.noreply.github.com> by github-actions[bot]
- fix: add missing type for allowAbsoluteUrls (#6818)

* fix: add missing type for allowAbsoluteUrls

* fix: use semicolon in type files

---------

Co-authored-by: Jay <jasonsaayman@gmail.com> by StefanBRas
- docs: update readme to include bun install (#6811)

Co-authored-by: Jay <jasonsaayman@gmail.com> by Ashcon Partovi
- fix(xhr/fetch): pass `allowAbsoluteUrls` to `buildFullPath` in `xhr` and `fetch` adapters (#6814) by Marc Hassan
- chore(release): v1.8.2 (#6812)

Co-authored-by: jasonsaayman <4814473+jasonsaayman@users.noreply.github.com> by github-actions[bot]
- fix(http-adapter): add allowAbsoluteUrls to path building (#6810)

Co-authored-by: alex-paystack <alex@paystack.com> by Fasoro-Joseph Alexander
- chore(sponsor): update sponsor block (#6804)

Co-authored-by: DigitalBrainJS <12586868+DigitalBrainJS@users.noreply.github.com> by github-actions[bot]
- chore(sponsor): update sponsor block (#6794)

Co-authored-by: DigitalBrainJS <12586868+DigitalBrainJS@users.noreply.github.com>
Co-authored-by: Dmitriy Mozgovoy <robotshara@gmail.com> by github-actions[bot]
- chore(release): v1.8.1 (#6800)

Co-authored-by: jasonsaayman <4814473+jasonsaayman@users.noreply.github.com> by github-actions[bot]
- fix(utils): move `generateString` to platform utils to avoid importing crypto module into client builds; (#6789)

* chore(ci): Add release-it script;

* fix(utils): move generateString util to platform utils to avoid importing crypto module into client build;

---------

Co-authored-by: Jay <jasonsaayman@gmail.com> by Dmitriy Mozgovoy
- chore(release): v1.8.0 (#6795)

Co-authored-by: jasonsaayman <4814473+jasonsaayman@users.noreply.github.com> by github-actions[bot]
- fix(utils): replace getRandomValues with crypto module (#6788) by Willian Agostini
- feat: Add config for ignoring absolute URLs (#5902) (#6192)

* fix: prevent request url override

prevent request URL from overriding preconfigured base URL

BREAKING CHANGE: code relying on the above will now combine the URLs instead of prefer request URL

* feat: add config option for allowing absolute URLs

* fix: add default value for allowAbsoluteUrls in buildFullPath

* fix: typo in flow control when setting allowAbsoluteUrls

* feat: update tests supporting issue #5902 functionality

* feat: update README.md with allowAbsoluteUrls

* fix: properly group conditions in buildFullPath.js to avoid undefined error when baseUrl undefined

* Update README.md fix typo

* fix: update build full path logic to address failing test case

* fix: update base URL test

* fix: remove problem test (works locally, will not work in the pipeline)

* fix: update https test to use github.com instead of google.com

* fix: revert previous commit

* fix: add back problem test

* chore: remove un-needed passed var to URL class instanciation

---------

Co-authored-by: Austin Ryan Lawson <ryan.lawson2@gmail.com>
Co-authored-by: Jay <jasonsaayman@gmail.com> by Michael Toscano
- chore(config): adjust rollup config to preserve license header to minified JavaScript (#6777) by Willian Agostini
- docs(type): fix typo in index.ts (#6030)

docs(type): fix typo in index.ts (#6030) by Habip Akyol
- test(transform): add test case for issue 5853 on response type to 'json' (#5901)

* test(transform): add test case for issue 5853 on response type to 'json'

* test(transform): formatted second argument

---------

Co-authored-by: Jay <jasonsaayman@gmail.com> by Naron
- chore(docs): typo in README (#6771)

chore(docs): typo in README (#6771) by Bailey Lissington
