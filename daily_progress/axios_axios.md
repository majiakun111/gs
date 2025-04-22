# axios Daily Progress.
## Issues
- fix(core): fix the Axios constructor implementation to treat the config argument as optional; (closed)
- Response interceptor calls success on 404, documentation differs (closed)
- Wrongly typed config parameter in constructor (closed)
- fix(headers): fix `getSetCookie` by using 'get' for caseless access; (closed)
- fix(headers): allow iterable objects to be a data source for the set method; (closed)
- [ DELETED ] (closed)
- Allow method-specific timeout configuration in axios.create (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- Release 0.30.0 should be marked as a patched version for GHSA-jr5f-v2jv-69x6 (closed)
- Error: header name must be a non-empty string (closed)
- fix(types): no auto complete for adapters (closed)
- bug: no autocomplete in adapter (closed)
- Ignore (closed)
- v0.x - AxiosRequestConfig is missing allowAbsoluteUrls (closed)
- add allowAbsoluteUrls type (closed)
- Axios 1.8.3 version has high security risk (closed)
- Axios is vulnerable to a server-side request forgery (SSRF) issue due to how absolute URLs that are passed to Axios are handled (closed)
- [Release] v1.8.4 (closed)
- Low-risk vulnerability - Version Disclosure (closed)
- OSS security Vulnerability in 1.8.3 (closed)
- High Security issues with axios (closed)
- chore(deps): bump tj-actions/changed-files from 45 to 46 in the github-actions group (closed)
- fix(canceled-error): break cyclic reference to prevent JSON.stringify… (closed)
- [Chore] Update sponsor block (closed)
- fix(buildFullPath): handle `allowAbsoluteUrls: false` without `baseURL` (closed)
- `TypeError` when specifying `allowAbsoluteUrls: false` without `baseURL` (closed)
- [Security] Backport SSRF vulnerability fix (CVE-2024-39338) to 0.x branch (closed)
- [Chore] Update sponsor block (closed)

## Pull Requests
- fix(core): fix the Axios constructor implementation to treat the config argument as optional; (closed)
- fix(headers): fix `getSetCookie` by using 'get' for caseless access; (closed)
- fix(headers): allow iterable objects to be a data source for the set method; (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- fix(types): no auto complete for adapters (closed)
- Ignore (closed)
- add allowAbsoluteUrls type (closed)
- [Release] v1.8.4 (closed)
- chore(deps): bump tj-actions/changed-files from 45 to 46 in the github-actions group (closed)
- fix(canceled-error): break cyclic reference to prevent JSON.stringify… (closed)
- [Chore] Update sponsor block (closed)
- fix(buildFullPath): handle `allowAbsoluteUrls: false` without `baseURL` (closed)
- [Chore] Update sponsor block (closed)
- Backport allowAbsoluteUrls vuln fix to v0.x (closed)
- [Chore] Update sponsor block (closed)
- Backport axios vuln fix (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- [Release] v1.8.3 (closed)
- fix: add missing type for allowAbsoluteUrls (closed)
- fix(xhr/fetch): pass `allowAbsoluteUrls` to `buildFullPath` in `xhr` and `fetch` adapters (closed)
- [Release] v1.8.2 (closed)
- docs: update readme to include bun install (closed)
- fix(http-adapter): add allowAbsoluteUrls to path building (closed)
- [Chore] Update sponsor block (closed)
- [Chore] Update sponsor block (closed)
- [Release] v1.8.1 (closed)
- Revert "fix(utils): replace getRandomValues with crypto module (#6788)" (closed)

## Commits
- fix(types): fix autocomplete for adapter config (#6855)

Co-authored-by: Dmitriy Mozgovoy <robotshara@gmail.com> by FatahChan
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
