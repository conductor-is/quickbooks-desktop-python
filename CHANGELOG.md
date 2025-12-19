# Changelog

## 1.67.1 (2025-12-19)

Full Changelog: [v1.67.0...v1.67.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.67.0...v1.67.1)

### Bug Fixes

* use async_to_httpx_files in patch method ([5c56f84](https://github.com/conductor-is/quickbooks-desktop-python/commit/5c56f84cf59bf52ddc328543e9bad441835d0fc7))


### Chores

* **internal:** add `--fix` argument to lint script ([5abda0b](https://github.com/conductor-is/quickbooks-desktop-python/commit/5abda0b19a6fecd21d943a5a716478863f95984d))

## 1.67.0 (2025-12-17)

Full Changelog: [v1.66.0...v1.67.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.66.0...v1.67.0)

### Features

* **api:** api update ([4f8b34a](https://github.com/conductor-is/quickbooks-desktop-python/commit/4f8b34a515be299063aa60084453ce3511c4be24))
* **api:** api update ([f63ed41](https://github.com/conductor-is/quickbooks-desktop-python/commit/f63ed41f819c6e73f5eba64c2fb9342d0ef3eb64))


### Chores

* **internal:** add missing files argument to base client ([360b761](https://github.com/conductor-is/quickbooks-desktop-python/commit/360b761de9bb6e18a09505ea0c1fc3d78d30dd48))
* speedup initial import ([4ec9e58](https://github.com/conductor-is/quickbooks-desktop-python/commit/4ec9e5820c25ebdcfcd394d0e4350492187bfaf2))

## 1.66.0 (2025-12-11)

Full Changelog: [v1.65.1...v1.66.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.65.1...v1.66.0)

### Features

* **api:** api update ([d54b73a](https://github.com/conductor-is/quickbooks-desktop-python/commit/d54b73a3775f20312b1c933ae12640eb783f9697))

## 1.65.1 (2025-12-10)

Full Changelog: [v1.65.0...v1.65.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.65.0...v1.65.1)

### Bug Fixes

* **types:** allow pyright to infer TypedDict types within SequenceNotStr ([2526110](https://github.com/conductor-is/quickbooks-desktop-python/commit/2526110c4b7875597b3eef1ec9223dab03fc38a6))


### Chores

* add missing docstrings ([920c79c](https://github.com/conductor-is/quickbooks-desktop-python/commit/920c79c6acd2574ed6f27229684fee0ece670ed2))

## 1.65.0 (2025-12-08)

Full Changelog: [v1.64.1...v1.65.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.64.1...v1.65.0)

### Features

* **api:** api update ([d29dfa4](https://github.com/conductor-is/quickbooks-desktop-python/commit/d29dfa412e648006d8636e410bbaf1298b48d287))


### Bug Fixes

* ensure streams are always closed ([9ca25fc](https://github.com/conductor-is/quickbooks-desktop-python/commit/9ca25fcf788b040f97ae88245b50df6d6cdb02f2))


### Chores

* add Python 3.14 classifier and testing ([c186982](https://github.com/conductor-is/quickbooks-desktop-python/commit/c186982182d758ce54c586b3317db2ebb7848eb1))
* **deps:** mypy 1.18.1 has a regression, pin to 1.17 ([73df7b5](https://github.com/conductor-is/quickbooks-desktop-python/commit/73df7b5876bb67359746699cf6f514b6dc41e1c8))
* **docs:** use environment variables for authentication in code snippets ([fe17ff5](https://github.com/conductor-is/quickbooks-desktop-python/commit/fe17ff56342667a1295007f93cb0049c6057dd06))
* update lockfile ([cb4e614](https://github.com/conductor-is/quickbooks-desktop-python/commit/cb4e61495ca42df21841c00ce8d697d35b51d2f6))

## 1.64.1 (2025-11-17)

Full Changelog: [v1.64.0...v1.64.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.64.0...v1.64.1)

### Bug Fixes

* **client:** close streams without requiring full consumption ([25f061f](https://github.com/conductor-is/quickbooks-desktop-python/commit/25f061faff03aba210ea1a4365d4017885471756))
* compat with Python 3.14 ([dc06a1c](https://github.com/conductor-is/quickbooks-desktop-python/commit/dc06a1c40d042058fce3466f5f8f310413c2b7e1))
* **compat:** update signatures of `model_dump` and `model_dump_json` for Pydantic v1 ([b67cc2e](https://github.com/conductor-is/quickbooks-desktop-python/commit/b67cc2e5fd532a5ec5ec9b64f142effbe554a854))


### Chores

* **internal/tests:** avoid race condition with implicit client cleanup ([aca514b](https://github.com/conductor-is/quickbooks-desktop-python/commit/aca514b98a59ffe8143dffbc63efa579c47530d0))
* **internal:** grammar fix (it's -&gt; its) ([f454485](https://github.com/conductor-is/quickbooks-desktop-python/commit/f4544851d79cae496c49ca0a86e7d6ef82fcf6ca))
* **package:** drop Python 3.8 support ([9e43537](https://github.com/conductor-is/quickbooks-desktop-python/commit/9e435376b9893f8104ff371f2054ed43db34900e))

## 1.64.0 (2025-10-20)

Full Changelog: [v1.63.0...v1.64.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.63.0...v1.64.0)

### Features

* **api:** api update ([d06f1d4](https://github.com/conductor-is/quickbooks-desktop-python/commit/d06f1d4437d242c25a2229da45c077d9bbe1cb6a))

## 1.63.0 (2025-10-18)

Full Changelog: [v1.62.0...v1.63.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.62.0...v1.63.0)

### Features

* **api:** api update ([b6301a7](https://github.com/conductor-is/quickbooks-desktop-python/commit/b6301a7690d1cbb45614360cdf321806c111d06f))
* **api:** api update ([e67b38c](https://github.com/conductor-is/quickbooks-desktop-python/commit/e67b38ce35fcf271a4f3900771056fd26076d579))
* **api:** api update ([fbfa9de](https://github.com/conductor-is/quickbooks-desktop-python/commit/fbfa9decdbcaa0dd4a431adc31fea2f53ee1c843))
* **api:** api update ([ae9197e](https://github.com/conductor-is/quickbooks-desktop-python/commit/ae9197eeaf0e9cacd2cb1593f185816ff1549d8b))


### Chores

* bump `httpx-aiohttp` version to 0.1.9 ([f266557](https://github.com/conductor-is/quickbooks-desktop-python/commit/f2665579329f848529204581aad0a4d357650e7f))
* **internal:** detect missing future annotations with ruff ([aad6657](https://github.com/conductor-is/quickbooks-desktop-python/commit/aad6657294e9a35eb01d66625c7a1e862aacc242))

## 1.62.0 (2025-10-06)

Full Changelog: [v1.61.1...v1.62.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.61.1...v1.62.0)

### Features

* **api:** api update ([c5c3a7b](https://github.com/conductor-is/quickbooks-desktop-python/commit/c5c3a7b4663022a769fbd6004972ccb0babcc2e3))


### Chores

* do not install brew dependencies in ./scripts/bootstrap by default ([d816d45](https://github.com/conductor-is/quickbooks-desktop-python/commit/d816d456537cf1aaf3a629cb1950e9e115577fd4))

## 1.61.1 (2025-09-19)

Full Changelog: [v1.61.0...v1.61.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.61.0...v1.61.1)

### Chores

* **types:** change optional parameter type from NotGiven to Omit ([d35ccbc](https://github.com/conductor-is/quickbooks-desktop-python/commit/d35ccbc68d64c61bfa6d1dad59adcaed870de2ca))

## 1.61.0 (2025-09-17)

Full Changelog: [v1.60.0...v1.61.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.60.0...v1.61.0)

### Features

* **api:** api update ([a9a9ad9](https://github.com/conductor-is/quickbooks-desktop-python/commit/a9a9ad977bcdac53e8b1ac1e5df7dc2bb0290938))

## 1.60.0 (2025-09-17)

Full Changelog: [v1.59.0...v1.60.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.59.0...v1.60.0)

### Features

* **api:** api update ([acc7713](https://github.com/conductor-is/quickbooks-desktop-python/commit/acc7713843dfadb942a143cc006591a470a2bf31))


### Chores

* **internal:** update pydantic dependency ([4079543](https://github.com/conductor-is/quickbooks-desktop-python/commit/4079543fd3091604fbd719f6b9f03acd158ac215))

## 1.59.0 (2025-09-16)

Full Changelog: [v1.58.1...v1.59.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.58.1...v1.59.0)

### Features

* **api:** api update ([7416245](https://github.com/conductor-is/quickbooks-desktop-python/commit/7416245cd2dd0cb7d51befc923198127c67a4282))

## 1.58.1 (2025-09-05)

Full Changelog: [v1.58.0...v1.58.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.58.0...v1.58.1)

### Chores

* **internal:** move mypy configurations to `pyproject.toml` file ([616d4d4](https://github.com/conductor-is/quickbooks-desktop-python/commit/616d4d4193aa82ac14d709d0a90fcbd0b0b92b1b))
* **tests:** simplify `get_platform` test ([2fa8c59](https://github.com/conductor-is/quickbooks-desktop-python/commit/2fa8c596bdddef326ae62d9e6d1863488ee9d1bb))

## 1.58.0 (2025-09-04)

Full Changelog: [v1.57.0...v1.58.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.57.0...v1.58.0)

### Features

* **api:** api update ([b725b5b](https://github.com/conductor-is/quickbooks-desktop-python/commit/b725b5b4b295ee3d2557ab9d5b0b1147829ef03e))
* improve future compat with pydantic v3 ([8c2a3e0](https://github.com/conductor-is/quickbooks-desktop-python/commit/8c2a3e04da4ad630d1d2c18c943b48562c26adae))
* **types:** replace List[str] with SequenceNotStr in params ([1e9040a](https://github.com/conductor-is/quickbooks-desktop-python/commit/1e9040a18f9d9ee9338fdff9e26175b0c879b55f))


### Chores

* **internal:** add Sequence related utils ([8247e7a](https://github.com/conductor-is/quickbooks-desktop-python/commit/8247e7ab2dc265aa8a1d258ee2a8d2c0603f27fa))

## 1.57.0 (2025-08-27)

Full Changelog: [v1.56.1...v1.57.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.56.1...v1.57.0)

### Features

* **api:** api update ([dfb676b](https://github.com/conductor-is/quickbooks-desktop-python/commit/dfb676bc51244ab2de1331fda57297ea831d45f8))
* **api:** api update ([87370fa](https://github.com/conductor-is/quickbooks-desktop-python/commit/87370fa494328717670db79e1f0a539d4df8cb6a))
* **api:** api update ([6352779](https://github.com/conductor-is/quickbooks-desktop-python/commit/6352779d091dcdb4fe0497b88c7f4a205581aee0))

## 1.56.1 (2025-08-27)

Full Changelog: [v1.56.0...v1.56.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.56.0...v1.56.1)

### Bug Fixes

* avoid newer type syntax ([bf6a51d](https://github.com/conductor-is/quickbooks-desktop-python/commit/bf6a51da6a79923d873112cd9403535bf640ca38))


### Chores

* **internal:** update pyright exclude list ([454adf3](https://github.com/conductor-is/quickbooks-desktop-python/commit/454adf3ace0ac9dafac5bce6c95bfb2855fd5092))

## 1.56.0 (2025-08-27)

Full Changelog: [v1.55.0...v1.56.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.55.0...v1.56.0)

### Features

* **api:** api update ([5023010](https://github.com/conductor-is/quickbooks-desktop-python/commit/50230106fb9d07eee925dc7381832b047072cffa))
* **api:** api update ([2bc878e](https://github.com/conductor-is/quickbooks-desktop-python/commit/2bc878e0ca0e6609593e0c60559709105f88da7f))
* **api:** api update ([c8e9fb7](https://github.com/conductor-is/quickbooks-desktop-python/commit/c8e9fb7e54d8c214897e09bd358adebed4bd01a7))
* **api:** api update ([ba33659](https://github.com/conductor-is/quickbooks-desktop-python/commit/ba33659e72b640fb1d3da1ad28ee48ab9c7072d3))


### Chores

* **internal:** change ci workflow machines ([0757734](https://github.com/conductor-is/quickbooks-desktop-python/commit/07577343b148b7fd47b4848067e4b396795be413))
* update github action ([586afe5](https://github.com/conductor-is/quickbooks-desktop-python/commit/586afe546d7544d32d4be78fe4eed965d2150284))

## 1.55.0 (2025-08-20)

Full Changelog: [v1.54.0...v1.55.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.54.0...v1.55.0)

### Features

* **api:** api update ([f790521](https://github.com/conductor-is/quickbooks-desktop-python/commit/f790521b6ca6e25780fe387baa1affddfc9d930e))

## 1.54.0 (2025-08-16)

Full Changelog: [v1.53.0...v1.54.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.53.0...v1.54.0)

### Features

* **api:** api update ([8bfccf5](https://github.com/conductor-is/quickbooks-desktop-python/commit/8bfccf5f30ad5b9bd99cab18b0aa6056469aa3b3))
* **api:** api update ([b4d33a9](https://github.com/conductor-is/quickbooks-desktop-python/commit/b4d33a90669ea36256298409530c7ef5e2ad4f00))
* **api:** api update ([5439e4f](https://github.com/conductor-is/quickbooks-desktop-python/commit/5439e4f6ae75b3f2db3eaefbc0fdf979a3aea02f))
* **api:** api update ([857745c](https://github.com/conductor-is/quickbooks-desktop-python/commit/857745cf1914e9af48a5002e59bff7a39a8aad42))
* **api:** api update ([e9dbff2](https://github.com/conductor-is/quickbooks-desktop-python/commit/e9dbff2d153705ef7b2a503ffe8ee68408b6a08c))

## 1.53.0 (2025-08-15)

Full Changelog: [v1.52.0...v1.53.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.52.0...v1.53.0)

### Features

* **api:** api update ([26c064e](https://github.com/conductor-is/quickbooks-desktop-python/commit/26c064e8fa11a333546a72e5b077ecc95a159535))

## 1.52.0 (2025-08-15)

Full Changelog: [v1.51.0...v1.52.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.51.0...v1.52.0)

### Features

* **api:** api update ([3c54e1e](https://github.com/conductor-is/quickbooks-desktop-python/commit/3c54e1eaa54a97253de2e2b306c515ea06943660))
* **api:** api update ([9cd68b6](https://github.com/conductor-is/quickbooks-desktop-python/commit/9cd68b62c70712ac8ddaa992c21fc28166d4828d))
* **api:** api update ([0b9357f](https://github.com/conductor-is/quickbooks-desktop-python/commit/0b9357fd121c030a9846216630af7556982da943))
* **api:** api update ([3733063](https://github.com/conductor-is/quickbooks-desktop-python/commit/3733063ee6f1c3774cc12fe0f3c9edae30d8c029))

## 1.51.0 (2025-08-12)

Full Changelog: [v1.50.0...v1.51.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.50.0...v1.51.0)

### Features

* **api:** api update ([a1fe919](https://github.com/conductor-is/quickbooks-desktop-python/commit/a1fe91958c1f1029d7d68c6eafa84211ad36c063))


### Chores

* **internal:** fix ruff target version ([39741fc](https://github.com/conductor-is/quickbooks-desktop-python/commit/39741fca93e01e0558b3910aaeec7b03167abad1))
* **internal:** update comment in script ([e6dd8ea](https://github.com/conductor-is/quickbooks-desktop-python/commit/e6dd8ea28004698c120905f0d1f1bd2216cb1711))
* update @stainless-api/prism-cli to v5.15.0 ([0372289](https://github.com/conductor-is/quickbooks-desktop-python/commit/0372289774ddd8af2aed8adbc830a59b18750981))

## 1.50.0 (2025-08-04)

Full Changelog: [v1.49.0...v1.50.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.49.0...v1.50.0)

### Features

* **api:** api update ([827e615](https://github.com/conductor-is/quickbooks-desktop-python/commit/827e615c4822d13e1bdf83aa4e8bae6a85a3f97a))
* **api:** api update ([b50ad50](https://github.com/conductor-is/quickbooks-desktop-python/commit/b50ad50ff19673baa5925466d92b80bbbe781d17))

## 1.49.0 (2025-08-01)

Full Changelog: [v1.48.0...v1.49.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.48.0...v1.49.0)

### Features

* **api:** api update ([0da0b31](https://github.com/conductor-is/quickbooks-desktop-python/commit/0da0b31f58ea29496f90b8a45581a8e3f280d1a9))
* **api:** api update ([d115916](https://github.com/conductor-is/quickbooks-desktop-python/commit/d11591663434dc944585056adfa88d571e9d0ea0))

## 1.48.0 (2025-08-01)

Full Changelog: [v1.47.0...v1.48.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.47.0...v1.48.0)

### Features

* **api:** api update ([db74a07](https://github.com/conductor-is/quickbooks-desktop-python/commit/db74a079235a54760f50f99d2a326e6ebef8b4fb))
* **client:** support file upload requests ([edd60ef](https://github.com/conductor-is/quickbooks-desktop-python/commit/edd60ef070aea15de6812c3cfcb542b808a4fd9a))


### Chores

* **project:** add settings file for vscode ([6fd7534](https://github.com/conductor-is/quickbooks-desktop-python/commit/6fd75344923fdf1335b67503ec008706520d8ee6))

## 1.47.0 (2025-07-23)

Full Changelog: [v1.46.0...v1.47.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.46.0...v1.47.0)

### Features

* **api:** api update ([e205c9e](https://github.com/conductor-is/quickbooks-desktop-python/commit/e205c9e685f68581498d6413481921f01fa49d9c))


### Bug Fixes

* **parsing:** ignore empty metadata ([2b58924](https://github.com/conductor-is/quickbooks-desktop-python/commit/2b5892426fc9ba4c48c518ec36e5ab541f4ab35d))
* **parsing:** parse extra field types ([235f6af](https://github.com/conductor-is/quickbooks-desktop-python/commit/235f6af1af18879228161495398e76e17d14bf21))

## 1.46.0 (2025-07-21)

Full Changelog: [v1.45.0...v1.46.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.45.0...v1.46.0)

### Features

* **api:** api update ([1d12064](https://github.com/conductor-is/quickbooks-desktop-python/commit/1d120646587e93537d6aca641c82ac07c605c3fa))

## 1.45.0 (2025-07-18)

Full Changelog: [v1.44.1...v1.45.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.44.1...v1.45.0)

### Features

* **api:** api update ([8e86019](https://github.com/conductor-is/quickbooks-desktop-python/commit/8e86019d44279acc9c3dd8779905cca636b23ff3))
* clean up environment call outs ([10c53db](https://github.com/conductor-is/quickbooks-desktop-python/commit/10c53db09277343344371351c171bba3e8c6faed))


### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([e01c352](https://github.com/conductor-is/quickbooks-desktop-python/commit/e01c352e460e25eb647cc8edf030068585dc5c35))


### Chores

* **readme:** fix version rendering on pypi ([8317c58](https://github.com/conductor-is/quickbooks-desktop-python/commit/8317c58e8468ce8f16b28283759330adfefccfba))

## 1.44.1 (2025-07-11)

Full Changelog: [v1.44.0...v1.44.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.44.0...v1.44.1)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([e9bf1ed](https://github.com/conductor-is/quickbooks-desktop-python/commit/e9bf1ed9844b5de8d382cef959f2fecf372db84c))

### Chores

* **internal:** bump pinned h11 dep ([723555a](https://github.com/conductor-is/quickbooks-desktop-python/commit/723555a9e7b9386fb43231b2a32731ade2fa54b8))
* **package:** mark python 3.13 as supported ([db30310](https://github.com/conductor-is/quickbooks-desktop-python/commit/db30310480b267d89997b8642bda2f47a66920fa))
* **readme:** fix version rendering on PyPI ([906b22a](https://github.com/conductor-is/quickbooks-desktop-python/commit/906b22a5da3caf8af905eacc55e479c781076d47))

## 1.44.0 (2025-07-08)

Full Changelog: [v1.43.0...v1.44.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.43.0...v1.44.0)

### Features

* **api:** api update ([ac819f7](https://github.com/conductor-is/quickbooks-desktop-python/commit/ac819f753e81ceb64843a4a66b5a2e9d9723fd58))


### Bug Fixes

* **ci:** correct conditional ([87462db](https://github.com/conductor-is/quickbooks-desktop-python/commit/87462db3c1434b0ed1718a55fc274a4aa61dbd84))


### Chores

* **ci:** change upload type ([d1325f0](https://github.com/conductor-is/quickbooks-desktop-python/commit/d1325f0c663b1213f9097291f6bec83f6776b02b))
* **ci:** only run for pushes and fork pull requests ([6a4b7a6](https://github.com/conductor-is/quickbooks-desktop-python/commit/6a4b7a62caf82f3892265e88196dbb4bb2f717f5))
* **internal:** codegen related update ([8078db3](https://github.com/conductor-is/quickbooks-desktop-python/commit/8078db3fbb7c2b5801e49497ad71fde6f16f1864))

## 1.43.0 (2025-06-27)

Full Changelog: [v1.42.0...v1.43.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.42.0...v1.43.0)

### Features

* **api:** api update ([7bff10f](https://github.com/conductor-is/quickbooks-desktop-python/commit/7bff10ff10eb2398072a409955f7c3fbc8ac788f))
* **client:** add support for aiohttp ([fa886b5](https://github.com/conductor-is/quickbooks-desktop-python/commit/fa886b5e097bbdc15db5bd13b3e6ec139ac80666))


### Bug Fixes

* **ci:** release-doctor — report correct token name ([42ef854](https://github.com/conductor-is/quickbooks-desktop-python/commit/42ef85421254b9e6bbaba12ef1f8d5ee8215b37b))


### Chores

* **tests:** skip some failing tests on the latest python versions ([1586ccb](https://github.com/conductor-is/quickbooks-desktop-python/commit/1586ccb8991c3b854a20010823ef65849d0a7d18))

## 1.42.0 (2025-06-19)

Full Changelog: [v1.41.0...v1.42.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.41.0...v1.42.0)

### Features

* **api:** api update ([d73b209](https://github.com/conductor-is/quickbooks-desktop-python/commit/d73b209ea6cccac0d2c00a9e7143499bb15426dc))


### Bug Fixes

* **client:** correctly parse binary response | stream ([ff3e590](https://github.com/conductor-is/quickbooks-desktop-python/commit/ff3e590a7f74562f6f157d572347aef3be51b897))


### Chores

* **ci:** enable for pull requests ([259dcd8](https://github.com/conductor-is/quickbooks-desktop-python/commit/259dcd89b886ec14be07197b1738983b680b8850))
* **internal:** update conftest.py ([1db5923](https://github.com/conductor-is/quickbooks-desktop-python/commit/1db59237859be3a5143527b06a1be7a6ffa48cb4))
* **readme:** update badges ([c37e361](https://github.com/conductor-is/quickbooks-desktop-python/commit/c37e361650ee5d781f0b1739715470e88f86cd51))
* **tests:** add tests for httpx client instantiation & proxies ([e41fa25](https://github.com/conductor-is/quickbooks-desktop-python/commit/e41fa25447e7cd80e98137bf378b793bc5efa249))
* **tests:** run tests in parallel ([58dde0e](https://github.com/conductor-is/quickbooks-desktop-python/commit/58dde0ec89210d597817651319a0a5f81ebc0673))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([457ad1e](https://github.com/conductor-is/quickbooks-desktop-python/commit/457ad1e81fd87881831c2db5dcbbb8413fd0fd0d))

## 1.41.0 (2025-06-10)

Full Changelog: [v1.40.0...v1.41.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.40.0...v1.41.0)

### Features

* **api:** api update ([57ecc43](https://github.com/conductor-is/quickbooks-desktop-python/commit/57ecc43922b210afd71b771fd60bc1626833601c))
* **client:** add follow_redirects request option ([c76d62a](https://github.com/conductor-is/quickbooks-desktop-python/commit/c76d62a469dc960b757c1f2c1f7944fb3eedc90e))


### Chores

* **docs:** grammar improvements ([408eb35](https://github.com/conductor-is/quickbooks-desktop-python/commit/408eb3521c15dfddff4c413aaaf5dd39008d2e77))
* **docs:** remove reference to rye shell ([9209782](https://github.com/conductor-is/quickbooks-desktop-python/commit/9209782cc1479d2a57084a2e090b0d09ed090fa4))
* **docs:** remove unnecessary param examples ([cf2e05b](https://github.com/conductor-is/quickbooks-desktop-python/commit/cf2e05b32e4f08fc9f905956c0235cc46349b920))

## 1.40.0 (2025-05-16)

Full Changelog: [v1.39.0...v1.40.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.39.0...v1.40.0)

### Features

* **api:** api update ([d633855](https://github.com/conductor-is/quickbooks-desktop-python/commit/d6338551b958146ab17ee2bb1d24ce3b6846b277))


### Bug Fixes

* **package:** support direct resource imports ([fe33d5f](https://github.com/conductor-is/quickbooks-desktop-python/commit/fe33d5f6bf376409cabe985ba2262d54b632f3cd))


### Chores

* **ci:** fix installation instructions ([9d07171](https://github.com/conductor-is/quickbooks-desktop-python/commit/9d071719474cfb0791fa7f9f1322c0750de91769))
* **ci:** upload sdks to package manager ([8c8eb0f](https://github.com/conductor-is/quickbooks-desktop-python/commit/8c8eb0fc482c1c761c8ef82a313cc9d18f11f3ba))
* **internal:** avoid errors for isinstance checks on proxies ([2f8fd83](https://github.com/conductor-is/quickbooks-desktop-python/commit/2f8fd8317964df9144ff877384072af02cc9253d))

## 1.39.0 (2025-05-08)

Full Changelog: [v1.38.0...v1.39.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.38.0...v1.39.0)

### Features

* **api:** api update ([4942894](https://github.com/conductor-is/quickbooks-desktop-python/commit/494289475049ff56a82eeeb0bfd4444a2ba045a4))

## 1.38.0 (2025-05-08)

Full Changelog: [v1.37.0...v1.38.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.37.0...v1.38.0)

### Features

* **api:** api update ([a8a01d6](https://github.com/conductor-is/quickbooks-desktop-python/commit/a8a01d69f7080d09e8a8d23ee0ba0a30f9b45eff))

## 1.37.0 (2025-05-07)

Full Changelog: [v1.36.0...v1.37.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.36.0...v1.37.0)

### Features

* **api:** api update ([d943d4c](https://github.com/conductor-is/quickbooks-desktop-python/commit/d943d4c05c6566ea9f123d6ee58ff47c54249f30))

## 1.36.0 (2025-05-06)

Full Changelog: [v1.35.0...v1.36.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.35.0...v1.36.0)

### Features

* **api:** api update ([a699baa](https://github.com/conductor-is/quickbooks-desktop-python/commit/a699baaf89f4850d502badbda950994ee222e064))

## 1.35.0 (2025-05-05)

Full Changelog: [v1.34.0...v1.35.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.34.0...v1.35.0)

### Features

* **api:** api update ([e001b4f](https://github.com/conductor-is/quickbooks-desktop-python/commit/e001b4fea9ba279c70b06ab4294c659961a72c42))


### Bug Fixes

* **pydantic v1:** more robust ModelField.annotation check ([024926b](https://github.com/conductor-is/quickbooks-desktop-python/commit/024926b582330cc9a75435f89c250988fe7158f4))


### Chores

* broadly detect json family of content-type headers ([001a1ba](https://github.com/conductor-is/quickbooks-desktop-python/commit/001a1ba69fa31a80bc1f81885592867f17a3c2cb))
* **ci:** add timeout thresholds for CI jobs ([5757fae](https://github.com/conductor-is/quickbooks-desktop-python/commit/5757fae231a11728d1e9278153dc4bd5ab2b098a))
* **ci:** only use depot for staging repos ([8a4509c](https://github.com/conductor-is/quickbooks-desktop-python/commit/8a4509c31acf4c0d95fa105f5042c85f5fffaa1c))
* **internal:** codegen related update ([26e32a5](https://github.com/conductor-is/quickbooks-desktop-python/commit/26e32a5475b5299b1db70f50d8c842e24fda2e96))
* **internal:** fix list file params ([be07999](https://github.com/conductor-is/quickbooks-desktop-python/commit/be079990b68669ea54cdab53966feb8f563eef42))
* **internal:** import reformatting ([ee7884c](https://github.com/conductor-is/quickbooks-desktop-python/commit/ee7884c22c3ea949591f0f612e9efcfc9c3f5c1b))
* **internal:** refactor retries to not use recursion ([32f6ed4](https://github.com/conductor-is/quickbooks-desktop-python/commit/32f6ed4adfd21a863c80b4d0e2c125a72b4e28ac))

## 1.34.0 (2025-04-23)

Full Changelog: [v1.33.0...v1.34.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.33.0...v1.34.0)

### Features

* **api:** api update ([64df6d6](https://github.com/conductor-is/quickbooks-desktop-python/commit/64df6d6d4463f358d095997c114f9dad2162f540))


### Chores

* **internal:** update models test ([42f7394](https://github.com/conductor-is/quickbooks-desktop-python/commit/42f73946058ae8ad93feccf8a2eb2526dc71c780))

## 1.33.0 (2025-04-18)

Full Changelog: [v1.32.0...v1.33.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.32.0...v1.33.0)

### Features

* **api:** api update ([2f273d3](https://github.com/conductor-is/quickbooks-desktop-python/commit/2f273d35fed89cb2cc7d414e73add3a098efa8de))

## 1.32.0 (2025-04-17)

Full Changelog: [v1.31.0...v1.32.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.31.0...v1.32.0)

### Features

* **api:** api update ([#681](https://github.com/conductor-is/quickbooks-desktop-python/issues/681)) ([1592110](https://github.com/conductor-is/quickbooks-desktop-python/commit/1592110f682d11be03d66e171b8fb3e3aa702284))


### Bug Fixes

* **perf:** optimize some hot paths ([6ab024e](https://github.com/conductor-is/quickbooks-desktop-python/commit/6ab024e509fd7a408991fcf04f5aaf147f7c038e))
* **perf:** skip traversing types for NotGiven values ([45b9f7b](https://github.com/conductor-is/quickbooks-desktop-python/commit/45b9f7b93e0ce4b585d11ddc5487cd274893c785))


### Chores

* **client:** minor internal fixes ([d0d2b5a](https://github.com/conductor-is/quickbooks-desktop-python/commit/d0d2b5aa0645d3ecf23c77cb60a33ceffbbc9d9e))
* **internal:** base client updates ([6b338b2](https://github.com/conductor-is/quickbooks-desktop-python/commit/6b338b25c4b15c91fb3b672d52cc443b755ed0bb))
* **internal:** bump pyright version ([2922ba3](https://github.com/conductor-is/quickbooks-desktop-python/commit/2922ba31aaa57bd82d9e7aba9bc2c9d1eeaa57d3))
* **internal:** codegen related update ([#683](https://github.com/conductor-is/quickbooks-desktop-python/issues/683)) ([5234f2a](https://github.com/conductor-is/quickbooks-desktop-python/commit/5234f2a30784f4b688548c9ff5b6cf3f60629867))
* **internal:** expand CI branch coverage ([e942c14](https://github.com/conductor-is/quickbooks-desktop-python/commit/e942c148279b2b9021c9bed92e53bcf884eee533))
* **internal:** reduce CI branch coverage ([1b9bc07](https://github.com/conductor-is/quickbooks-desktop-python/commit/1b9bc07ad468a56554d11222d2b6d8aac2ac3692))
* **internal:** remove trailing character ([#684](https://github.com/conductor-is/quickbooks-desktop-python/issues/684)) ([39f751c](https://github.com/conductor-is/quickbooks-desktop-python/commit/39f751cf1d6fc39b8b75f3aee83842a0d4226c0f))
* **internal:** slight transform perf improvement ([#685](https://github.com/conductor-is/quickbooks-desktop-python/issues/685)) ([11d8eb3](https://github.com/conductor-is/quickbooks-desktop-python/commit/11d8eb335f4444543cc87ccc399b7f1197132413))
* **internal:** update pyright settings ([35c2374](https://github.com/conductor-is/quickbooks-desktop-python/commit/35c237400d10c90f73734e92434bff28911a8843))
* **tests:** improve enum examples ([#686](https://github.com/conductor-is/quickbooks-desktop-python/issues/686)) ([496fc3a](https://github.com/conductor-is/quickbooks-desktop-python/commit/496fc3aac1f64ffc3a21b38af63f53a25cc44a96))


### Documentation

* remove private imports from datetime snippets ([3bbbd77](https://github.com/conductor-is/quickbooks-desktop-python/commit/3bbbd77c64f263ec9b469450d82fca980c4e312c))

## 1.31.0 (2025-03-27)

Full Changelog: [v1.30.0...v1.31.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.30.0...v1.31.0)

### Features

* **api:** api update ([#679](https://github.com/conductor-is/quickbooks-desktop-python/issues/679)) ([e725872](https://github.com/conductor-is/quickbooks-desktop-python/commit/e7258720cfdce800751b175ff274a70d35ebce31))


### Chores

* fix typos ([#677](https://github.com/conductor-is/quickbooks-desktop-python/issues/677)) ([b595686](https://github.com/conductor-is/quickbooks-desktop-python/commit/b595686c656ff42109ee0f45789f4a8cb243d925))

## 1.30.0 (2025-03-25)

Full Changelog: [v1.29.0...v1.30.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.29.0...v1.30.0)

### Features

* **api:** api update ([#674](https://github.com/conductor-is/quickbooks-desktop-python/issues/674)) ([010aca3](https://github.com/conductor-is/quickbooks-desktop-python/commit/010aca3578e8d136ffd0e71a830e9970f5d29314))

## 1.29.0 (2025-03-24)

Full Changelog: [v1.28.0...v1.29.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.28.0...v1.29.0)

### Features

* **api:** api update ([#671](https://github.com/conductor-is/quickbooks-desktop-python/issues/671)) ([acd9bbb](https://github.com/conductor-is/quickbooks-desktop-python/commit/acd9bbb211ff60323ea0dc791075e7e0e7b80864))

## 1.28.0 (2025-03-23)

Full Changelog: [v1.27.0...v1.28.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.27.0...v1.28.0)

### Features

* **api:** api update ([#668](https://github.com/conductor-is/quickbooks-desktop-python/issues/668)) ([dcfd17f](https://github.com/conductor-is/quickbooks-desktop-python/commit/dcfd17fbea1898c923b4d7877e4ce86f38ae30de))

## 1.27.0 (2025-03-23)

Full Changelog: [v1.26.0...v1.27.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.26.0...v1.27.0)

### Features

* **api:** api update ([#665](https://github.com/conductor-is/quickbooks-desktop-python/issues/665)) ([bffdafa](https://github.com/conductor-is/quickbooks-desktop-python/commit/bffdafac2421037fa2c450aa2a23a5c90160cab9))

## 1.26.0 (2025-03-20)

Full Changelog: [v1.25.0...v1.26.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.25.0...v1.26.0)

### Features

* **api:** api update ([#647](https://github.com/conductor-is/quickbooks-desktop-python/issues/647)) ([3652590](https://github.com/conductor-is/quickbooks-desktop-python/commit/3652590a0a9fc1fccaa7daab036d4ee81df760a2))
* **api:** api update ([#649](https://github.com/conductor-is/quickbooks-desktop-python/issues/649)) ([869747b](https://github.com/conductor-is/quickbooks-desktop-python/commit/869747bfff91a45d347e743f10036d6d8cf56374))
* **api:** api update ([#650](https://github.com/conductor-is/quickbooks-desktop-python/issues/650)) ([229fd19](https://github.com/conductor-is/quickbooks-desktop-python/commit/229fd1951a19ad670844074a6669b53d45d86ffd))
* **api:** api update ([#651](https://github.com/conductor-is/quickbooks-desktop-python/issues/651)) ([5524c3a](https://github.com/conductor-is/quickbooks-desktop-python/commit/5524c3a3445c2e80702c736fe0a10233f8728dba))
* **api:** api update ([#652](https://github.com/conductor-is/quickbooks-desktop-python/issues/652)) ([8088ff0](https://github.com/conductor-is/quickbooks-desktop-python/commit/8088ff06ecd451947d1e36063778a65c1025eb18))
* **api:** api update ([#653](https://github.com/conductor-is/quickbooks-desktop-python/issues/653)) ([35f6b93](https://github.com/conductor-is/quickbooks-desktop-python/commit/35f6b93b725d448eabfbd194f20521cde8dce37e))
* **api:** api update ([#654](https://github.com/conductor-is/quickbooks-desktop-python/issues/654)) ([82ffbcb](https://github.com/conductor-is/quickbooks-desktop-python/commit/82ffbcbdff19cbfbcf649bd3de83b42d43cb3aa8))
* **api:** api update ([#655](https://github.com/conductor-is/quickbooks-desktop-python/issues/655)) ([077a06d](https://github.com/conductor-is/quickbooks-desktop-python/commit/077a06d09e413343b1de1b8c8fbf96579af75d28))
* **api:** api update ([#656](https://github.com/conductor-is/quickbooks-desktop-python/issues/656)) ([68df2d5](https://github.com/conductor-is/quickbooks-desktop-python/commit/68df2d5b70a7a0c2d55efefae3c1f3f36df6da39))
* **api:** api update ([#657](https://github.com/conductor-is/quickbooks-desktop-python/issues/657)) ([203283b](https://github.com/conductor-is/quickbooks-desktop-python/commit/203283b46d283e135bbd1e911c66c69677568c1f))
* **api:** api update ([#658](https://github.com/conductor-is/quickbooks-desktop-python/issues/658)) ([67c50ee](https://github.com/conductor-is/quickbooks-desktop-python/commit/67c50eefc1b92d45f3f019f7b92d9f64d6f3501a))
* **api:** api update ([#659](https://github.com/conductor-is/quickbooks-desktop-python/issues/659)) ([af01e64](https://github.com/conductor-is/quickbooks-desktop-python/commit/af01e643192ba7d30af13d3e38417fa91e7b48a3))
* **api:** api update ([#660](https://github.com/conductor-is/quickbooks-desktop-python/issues/660)) ([e6f0f4e](https://github.com/conductor-is/quickbooks-desktop-python/commit/e6f0f4e398504775853984169a7420101a860ab5))
* **api:** api update ([#661](https://github.com/conductor-is/quickbooks-desktop-python/issues/661)) ([41782f9](https://github.com/conductor-is/quickbooks-desktop-python/commit/41782f9dd755fe25f80a4814844cc5c93fec68eb))
* **api:** api update ([#662](https://github.com/conductor-is/quickbooks-desktop-python/issues/662)) ([a3b41ca](https://github.com/conductor-is/quickbooks-desktop-python/commit/a3b41ca94dc79179623f52fe1f7463874384b529))
* **api:** api update ([#663](https://github.com/conductor-is/quickbooks-desktop-python/issues/663)) ([79fa993](https://github.com/conductor-is/quickbooks-desktop-python/commit/79fa9935ee616e1f1317ddea47285642443a3eef))

## 1.25.0 (2025-03-17)

Full Changelog: [v1.24.0...v1.25.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.24.0...v1.25.0)

### Features

* **api:** api update ([#645](https://github.com/conductor-is/quickbooks-desktop-python/issues/645)) ([f916bdc](https://github.com/conductor-is/quickbooks-desktop-python/commit/f916bdcec756d0d58899292769a141818698516d))


### Bug Fixes

* **ci:** ensure pip is always available ([#643](https://github.com/conductor-is/quickbooks-desktop-python/issues/643)) ([52c3fae](https://github.com/conductor-is/quickbooks-desktop-python/commit/52c3fae17b7865ef56aecfa759de4d9a2c3e931c))
* **ci:** remove publishing patch ([#644](https://github.com/conductor-is/quickbooks-desktop-python/issues/644)) ([4399c6b](https://github.com/conductor-is/quickbooks-desktop-python/commit/4399c6b15f6e4c71caac506627ca39b6d2748a7c))
* **types:** handle more discriminated union shapes ([#642](https://github.com/conductor-is/quickbooks-desktop-python/issues/642)) ([35cf4fd](https://github.com/conductor-is/quickbooks-desktop-python/commit/35cf4fd4e328944c48011f6111349d8df8efdce5))


### Chores

* **internal:** bump rye to 0.44.0 ([#640](https://github.com/conductor-is/quickbooks-desktop-python/issues/640)) ([d5b4822](https://github.com/conductor-is/quickbooks-desktop-python/commit/d5b4822633f715b4320896c6ed3482d74dbfdd7e))

## 1.24.0 (2025-03-15)

Full Changelog: [v1.23.0...v1.24.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.23.0...v1.24.0)

### Features

* **api:** api update ([#637](https://github.com/conductor-is/quickbooks-desktop-python/issues/637)) ([e397035](https://github.com/conductor-is/quickbooks-desktop-python/commit/e3970358873e70a1398f31e6c6518e2505146fa0))
* **api:** api update ([#638](https://github.com/conductor-is/quickbooks-desktop-python/issues/638)) ([b2ba46e](https://github.com/conductor-is/quickbooks-desktop-python/commit/b2ba46e93a6a1d96e7f599879ee9e6cf198842d2))


### Chores

* **internal:** remove extra empty newlines ([#635](https://github.com/conductor-is/quickbooks-desktop-python/issues/635)) ([68f9162](https://github.com/conductor-is/quickbooks-desktop-python/commit/68f9162514b12315325d0c0e860ca2ffac1b3053))

## 1.23.0 (2025-03-12)

Full Changelog: [v1.22.0...v1.23.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.22.0...v1.23.0)

### Features

* **api:** api update ([#628](https://github.com/conductor-is/quickbooks-desktop-python/issues/628)) ([9af9db8](https://github.com/conductor-is/quickbooks-desktop-python/commit/9af9db844d225e10d178e1ac91d24e464178fe2e))
* **api:** api update ([#630](https://github.com/conductor-is/quickbooks-desktop-python/issues/630)) ([0a67aec](https://github.com/conductor-is/quickbooks-desktop-python/commit/0a67aec3f90358f6b43671e9340f000fc8164419))
* **api:** api update ([#633](https://github.com/conductor-is/quickbooks-desktop-python/issues/633)) ([43d3b1b](https://github.com/conductor-is/quickbooks-desktop-python/commit/43d3b1b7697ed6e9d6beb0e99274ff99134ff9aa))


### Documentation

* revise readme docs about nested params ([#631](https://github.com/conductor-is/quickbooks-desktop-python/issues/631)) ([4401218](https://github.com/conductor-is/quickbooks-desktop-python/commit/4401218fef26cc4a07ac753b4e037ae7d59f85d7))

## 1.22.0 (2025-03-06)

Full Changelog: [v1.21.0...v1.22.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.21.0...v1.22.0)

### Features

* **api:** api update ([#625](https://github.com/conductor-is/quickbooks-desktop-python/issues/625)) ([e78d903](https://github.com/conductor-is/quickbooks-desktop-python/commit/e78d90313a5274d44f8ad24e3efc000baf31d4b1))

## 1.21.0 (2025-03-06)

Full Changelog: [v1.20.0...v1.21.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.20.0...v1.21.0)

### Features

* **api:** api update ([#620](https://github.com/conductor-is/quickbooks-desktop-python/issues/620)) ([216f957](https://github.com/conductor-is/quickbooks-desktop-python/commit/216f9574fd4dfd6415218c1748242cab9807d94c))
* **api:** api update ([#622](https://github.com/conductor-is/quickbooks-desktop-python/issues/622)) ([c1b1cef](https://github.com/conductor-is/quickbooks-desktop-python/commit/c1b1cef23547afe0c4c026e557751c37a0326316))
* **api:** api update ([#623](https://github.com/conductor-is/quickbooks-desktop-python/issues/623)) ([956645f](https://github.com/conductor-is/quickbooks-desktop-python/commit/956645f5de796ece5ea1187f7f578e6686f44fc8))

## 1.20.0 (2025-03-05)

Full Changelog: [v1.19.0...v1.20.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.19.0...v1.20.0)

### Features

* **api:** api update ([#612](https://github.com/conductor-is/quickbooks-desktop-python/issues/612)) ([61ff441](https://github.com/conductor-is/quickbooks-desktop-python/commit/61ff441284518d0d27ec2f5ea815f3c8a1a6ce2f))
* **api:** api update ([#613](https://github.com/conductor-is/quickbooks-desktop-python/issues/613)) ([182c4a2](https://github.com/conductor-is/quickbooks-desktop-python/commit/182c4a20e56deedcf7386211ba4a4b89d4bbbb87))
* **api:** api update ([#614](https://github.com/conductor-is/quickbooks-desktop-python/issues/614)) ([af7ef39](https://github.com/conductor-is/quickbooks-desktop-python/commit/af7ef3917206411ad9b635e9b81dd75e5020073a))
* **api:** api update ([#615](https://github.com/conductor-is/quickbooks-desktop-python/issues/615)) ([babbb51](https://github.com/conductor-is/quickbooks-desktop-python/commit/babbb51b96603044e583e263f525baf6894265ee))
* **api:** api update ([#616](https://github.com/conductor-is/quickbooks-desktop-python/issues/616)) ([c8e212b](https://github.com/conductor-is/quickbooks-desktop-python/commit/c8e212bb69a78f7bf82d29a88a81ba99bee30f47))
* **api:** api update ([#617](https://github.com/conductor-is/quickbooks-desktop-python/issues/617)) ([e23af32](https://github.com/conductor-is/quickbooks-desktop-python/commit/e23af32667a5e304c90c78f1424a51aeecfe05ac))
* **api:** api update ([#618](https://github.com/conductor-is/quickbooks-desktop-python/issues/618)) ([87ef281](https://github.com/conductor-is/quickbooks-desktop-python/commit/87ef28134d06da323b1f75488202ac6d98539788))


### Chores

* **docs:** update client docstring ([#609](https://github.com/conductor-is/quickbooks-desktop-python/issues/609)) ([e4b587b](https://github.com/conductor-is/quickbooks-desktop-python/commit/e4b587bfb96745094fd1b38f68343e6ed53367b0))
* **internal:** remove unused http client options forwarding ([#611](https://github.com/conductor-is/quickbooks-desktop-python/issues/611)) ([66fe818](https://github.com/conductor-is/quickbooks-desktop-python/commit/66fe8185276b32555ef21e379665cafee0bb9545))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([#608](https://github.com/conductor-is/quickbooks-desktop-python/issues/608)) ([9f76b5e](https://github.com/conductor-is/quickbooks-desktop-python/commit/9f76b5e77b212ca34bd3d6a97dd26c39c4fa9c39))

## 1.19.0 (2025-02-27)

Full Changelog: [v1.18.1...v1.19.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.18.1...v1.19.0)

### Features

* **api:** api update ([#603](https://github.com/conductor-is/quickbooks-desktop-python/issues/603)) ([1ab748e](https://github.com/conductor-is/quickbooks-desktop-python/commit/1ab748e22affdd257787b31f28c9b2ca802e5023))
* **api:** api update ([#605](https://github.com/conductor-is/quickbooks-desktop-python/issues/605)) ([ac3945e](https://github.com/conductor-is/quickbooks-desktop-python/commit/ac3945e1fc3665a72901025edf82208105a09ef9))
* **api:** api update ([#606](https://github.com/conductor-is/quickbooks-desktop-python/issues/606)) ([cc9fea2](https://github.com/conductor-is/quickbooks-desktop-python/commit/cc9fea254ed944696b06e1a498ab8ea0f950d0ac))

## 1.18.1 (2025-02-26)

Full Changelog: [v1.18.0...v1.18.1](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.18.0...v1.18.1)

### Chores

* **internal:** properly set __pydantic_private__ ([#600](https://github.com/conductor-is/quickbooks-desktop-python/issues/600)) ([c1bc69c](https://github.com/conductor-is/quickbooks-desktop-python/commit/c1bc69c5771f816e450daa09b3f6565934a570f5))

## 1.18.0 (2025-02-24)

Full Changelog: [v1.17.0...v1.18.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.17.0...v1.18.0)

### Features

* **api:** api update ([#596](https://github.com/conductor-is/quickbooks-desktop-python/issues/596)) ([555a04b](https://github.com/conductor-is/quickbooks-desktop-python/commit/555a04b0e7ef53ab3f78641decd8d41bff67d26e))
* **api:** api update ([#598](https://github.com/conductor-is/quickbooks-desktop-python/issues/598)) ([46c37d9](https://github.com/conductor-is/quickbooks-desktop-python/commit/46c37d901d916d341042d7e894b781b795f7971c))

## 1.17.0 (2025-02-24)

Full Changelog: [v1.16.0...v1.17.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.16.0...v1.17.0)

### Features

* **api:** api update ([#592](https://github.com/conductor-is/quickbooks-desktop-python/issues/592)) ([8d97acd](https://github.com/conductor-is/quickbooks-desktop-python/commit/8d97acdd9c129f67e0315a9c6a2e3aaa09f4f159))
* **api:** api update ([#594](https://github.com/conductor-is/quickbooks-desktop-python/issues/594)) ([9747ded](https://github.com/conductor-is/quickbooks-desktop-python/commit/9747dedc63556196e3c100451b60ffba0a53a9e4))

## 1.16.0 (2025-02-23)

Full Changelog: [v1.15.0...v1.16.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.15.0...v1.16.0)

### Features

* **api:** api update ([#589](https://github.com/conductor-is/quickbooks-desktop-python/issues/589)) ([8dafa2e](https://github.com/conductor-is/quickbooks-desktop-python/commit/8dafa2e92d74aee3a2f4e20d3b126a4f255fc02c))

## 1.15.0 (2025-02-23)

Full Changelog: [v1.14.0...v1.15.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.14.0...v1.15.0)

### Features

* **api:** api update ([#586](https://github.com/conductor-is/quickbooks-desktop-python/issues/586)) ([d0736fe](https://github.com/conductor-is/quickbooks-desktop-python/commit/d0736fed9e7314dedc82f7a947a00e8f15b40899))

## 1.14.0 (2025-02-23)

Full Changelog: [v1.13.0...v1.14.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.13.0...v1.14.0)

### Features

* **api:** api update ([#579](https://github.com/conductor-is/quickbooks-desktop-python/issues/579)) ([c5a335b](https://github.com/conductor-is/quickbooks-desktop-python/commit/c5a335bb6ec56021c6017f12886c1ead602bee52))
* **api:** api update ([#582](https://github.com/conductor-is/quickbooks-desktop-python/issues/582)) ([5b88938](https://github.com/conductor-is/quickbooks-desktop-python/commit/5b8893859d6567f7014bdde5eb69a87ca825bded))
* **api:** api update ([#583](https://github.com/conductor-is/quickbooks-desktop-python/issues/583)) ([ceb33c5](https://github.com/conductor-is/quickbooks-desktop-python/commit/ceb33c573012d1188dc1b7a7f177f711e74661fa))
* **api:** api update ([#584](https://github.com/conductor-is/quickbooks-desktop-python/issues/584)) ([ee0bef1](https://github.com/conductor-is/quickbooks-desktop-python/commit/ee0bef199a5879574e67944956bb807e23236386))


### Chores

* **internal:** fix devcontainers setup ([#581](https://github.com/conductor-is/quickbooks-desktop-python/issues/581)) ([b9eca66](https://github.com/conductor-is/quickbooks-desktop-python/commit/b9eca660c89c0806310a3bf62657aec000a8041f))

## 1.13.0 (2025-02-21)

Full Changelog: [v1.12.0...v1.13.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.12.0...v1.13.0)

### Features

* **api:** api update ([#577](https://github.com/conductor-is/quickbooks-desktop-python/issues/577)) ([92da576](https://github.com/conductor-is/quickbooks-desktop-python/commit/92da576ad25f877dd5e8fa2688c875d1544475cf))
* **client:** allow passing `NotGiven` for body ([#575](https://github.com/conductor-is/quickbooks-desktop-python/issues/575)) ([bc4bd33](https://github.com/conductor-is/quickbooks-desktop-python/commit/bc4bd33de2fbbb709b7a9a3b2f742516f4f22d7f))


### Bug Fixes

* **client:** mark some request bodies as optional ([bc4bd33](https://github.com/conductor-is/quickbooks-desktop-python/commit/bc4bd33de2fbbb709b7a9a3b2f742516f4f22d7f))

## 1.12.0 (2025-02-19)

Full Changelog: [v1.11.0...v1.12.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.11.0...v1.12.0)

### Features

* **api:** api update ([#572](https://github.com/conductor-is/quickbooks-desktop-python/issues/572)) ([7c467ee](https://github.com/conductor-is/quickbooks-desktop-python/commit/7c467ee343eed457f6f3cc10ca6359dbe9225cf1))

## 1.11.0 (2025-02-18)

Full Changelog: [v1.10.0...v1.11.0](https://github.com/conductor-is/quickbooks-desktop-python/compare/v1.10.0...v1.11.0)

### Features

* **api:** api update ([#565](https://github.com/conductor-is/quickbooks-desktop-python/issues/565)) ([cd9d0f6](https://github.com/conductor-is/quickbooks-desktop-python/commit/cd9d0f6a442a50a5bcbeb533385d97aa01de3848))
* **api:** api update ([#568](https://github.com/conductor-is/quickbooks-desktop-python/issues/568)) ([a936bc7](https://github.com/conductor-is/quickbooks-desktop-python/commit/a936bc7f8a92d4aeab53d72bc82414300e15cbf4))
* **api:** api update ([#569](https://github.com/conductor-is/quickbooks-desktop-python/issues/569)) ([2374d08](https://github.com/conductor-is/quickbooks-desktop-python/commit/2374d0849ed255fa356a0fbfa5189571bd4f71c9))


### Bug Fixes

* asyncify on non-asyncio runtimes ([#567](https://github.com/conductor-is/quickbooks-desktop-python/issues/567)) ([aa8f795](https://github.com/conductor-is/quickbooks-desktop-python/commit/aa8f795c224a52873c40c9cc0f93e7e01a21d840))


### Chores

* **internal:** codegen related update ([#570](https://github.com/conductor-is/quickbooks-desktop-python/issues/570)) ([2bd484e](https://github.com/conductor-is/quickbooks-desktop-python/commit/2bd484e2f4a59813f5c0ea7f0c8d2451a35c9593))

## 1.10.0 (2025-02-13)

Full Changelog: [v1.9.1...v1.10.0](https://github.com/conductor-is/conductor-python/compare/v1.9.1...v1.10.0)

### Features

* **api:** api update ([#562](https://github.com/conductor-is/conductor-python/issues/562)) ([393404c](https://github.com/conductor-is/conductor-python/commit/393404caf3ace6528d8bdfbed4da508c1c9e3659))

## 1.9.1 (2025-02-10)

Full Changelog: [v1.9.0...v1.9.1](https://github.com/conductor-is/conductor-python/compare/v1.9.0...v1.9.1)

### Documentation

* **readme:** update example snippets ([#559](https://github.com/conductor-is/conductor-python/issues/559)) ([c740841](https://github.com/conductor-is/conductor-python/commit/c740841bd745e1e12c832eafa96df1efa9245b49))

## 1.9.0 (2025-02-07)

Full Changelog: [v1.8.0...v1.9.0](https://github.com/conductor-is/conductor-python/compare/v1.8.0...v1.9.0)

### Features

* **api:** api update ([#553](https://github.com/conductor-is/conductor-python/issues/553)) ([996879d](https://github.com/conductor-is/conductor-python/commit/996879d359a9707d0601d553a74538be4443cbd7))
* **api:** api update ([#554](https://github.com/conductor-is/conductor-python/issues/554)) ([43d38f2](https://github.com/conductor-is/conductor-python/commit/43d38f2d3d6e15d86de465730979fe8828b61821))
* **api:** api update ([#555](https://github.com/conductor-is/conductor-python/issues/555)) ([ed3f278](https://github.com/conductor-is/conductor-python/commit/ed3f2786d3d9e9688c574eecea2087158e4180eb))
* **api:** api update ([#556](https://github.com/conductor-is/conductor-python/issues/556)) ([61b195e](https://github.com/conductor-is/conductor-python/commit/61b195e84cf4c6546defe58769bfaf628ae37624))
* **api:** api update ([#557](https://github.com/conductor-is/conductor-python/issues/557)) ([6c9b241](https://github.com/conductor-is/conductor-python/commit/6c9b24138412d63235a8afc96295bae06972ecb6))


### Chores

* **internal:** fix type traversing dictionary params ([#550](https://github.com/conductor-is/conductor-python/issues/550)) ([1395adf](https://github.com/conductor-is/conductor-python/commit/1395adf3cefbaede27016dff3a80e6dfb8b1f8a1))
* **internal:** minor type handling changes ([#552](https://github.com/conductor-is/conductor-python/issues/552)) ([0f780e3](https://github.com/conductor-is/conductor-python/commit/0f780e3d74b3c7294be518302db4219cdb11eb6f))

## 1.8.0 (2025-02-06)

Full Changelog: [v1.7.0...v1.8.0](https://github.com/conductor-is/conductor-python/compare/v1.7.0...v1.8.0)

### Features

* **api:** api update ([#545](https://github.com/conductor-is/conductor-python/issues/545)) ([db14456](https://github.com/conductor-is/conductor-python/commit/db144565bc487ad4e9d64b1de4c9f7b98c7a8954))
* **api:** api update ([#547](https://github.com/conductor-is/conductor-python/issues/547)) ([8d6949d](https://github.com/conductor-is/conductor-python/commit/8d6949d1a845f913a081975d73704e156406e5ef))


### Chores

* **internal:** codegen related update ([#548](https://github.com/conductor-is/conductor-python/issues/548)) ([d8e18c9](https://github.com/conductor-is/conductor-python/commit/d8e18c9aaa7c527afcf395cbcd839cc591d93dc8))

## 1.7.0 (2025-02-04)

Full Changelog: [v1.6.0...v1.7.0](https://github.com/conductor-is/conductor-python/compare/v1.6.0...v1.7.0)

### Features

* **api:** api update ([#542](https://github.com/conductor-is/conductor-python/issues/542)) ([f8f232e](https://github.com/conductor-is/conductor-python/commit/f8f232ee0408f090b530a1d72de1f68baa91c1f0))

## 1.6.0 (2025-02-04)

Full Changelog: [v1.5.0...v1.6.0](https://github.com/conductor-is/conductor-python/compare/v1.5.0...v1.6.0)

### Features

* **api:** api update ([#540](https://github.com/conductor-is/conductor-python/issues/540)) ([77e158a](https://github.com/conductor-is/conductor-python/commit/77e158a6817363cafc876f6e6809de888866c576))


### Chores

* **internal:** bummp ruff dependency ([#539](https://github.com/conductor-is/conductor-python/issues/539)) ([cbae162](https://github.com/conductor-is/conductor-python/commit/cbae162d0ccc7c8ab8445cfe45be52d6563a0048))
* **internal:** change default timeout to an int ([#537](https://github.com/conductor-is/conductor-python/issues/537)) ([7e9cde3](https://github.com/conductor-is/conductor-python/commit/7e9cde36d0dbe201ec805d075906042453ca1b0c))

## 1.5.0 (2025-01-31)

Full Changelog: [v1.4.0...v1.5.0](https://github.com/conductor-is/conductor-python/compare/v1.4.0...v1.5.0)

### Features

* **api:** api update ([#528](https://github.com/conductor-is/conductor-python/issues/528)) ([c5145f6](https://github.com/conductor-is/conductor-python/commit/c5145f6e5c5004be88eadd73025c49c4f7ae5fdb))
* **api:** api update ([#530](https://github.com/conductor-is/conductor-python/issues/530)) ([6b301bc](https://github.com/conductor-is/conductor-python/commit/6b301bcc7882188e017f1c9ad249b1c13609a2f3))
* **api:** api update ([#531](https://github.com/conductor-is/conductor-python/issues/531)) ([babf254](https://github.com/conductor-is/conductor-python/commit/babf254c1995f92802839000203493deb55756ba))
* **api:** api update ([#532](https://github.com/conductor-is/conductor-python/issues/532)) ([8778641](https://github.com/conductor-is/conductor-python/commit/87786417fdb69f8fa9b74ea312eb5f20c44ef46a))
* **api:** api update ([#533](https://github.com/conductor-is/conductor-python/issues/533)) ([259d317](https://github.com/conductor-is/conductor-python/commit/259d317d07efc17bcb5d5dda4ea3845f743a019a))
* **api:** api update ([#534](https://github.com/conductor-is/conductor-python/issues/534)) ([1cd8125](https://github.com/conductor-is/conductor-python/commit/1cd81251f849b6cfc52dc32a1e044377c7208201))
* **api:** api update ([#535](https://github.com/conductor-is/conductor-python/issues/535)) ([0bb9786](https://github.com/conductor-is/conductor-python/commit/0bb9786934a54c6e56b4a38ed39cfb6a17a709ac))

## 1.4.0 (2025-01-29)

Full Changelog: [v1.3.0...v1.4.0](https://github.com/conductor-is/conductor-python/compare/v1.3.0...v1.4.0)

### Features

* **api:** api update ([#520](https://github.com/conductor-is/conductor-python/issues/520)) ([44cb588](https://github.com/conductor-is/conductor-python/commit/44cb588af56b52495227a0a9637c070c9f7c81e9))
* **api:** api update ([#522](https://github.com/conductor-is/conductor-python/issues/522)) ([f15ea45](https://github.com/conductor-is/conductor-python/commit/f15ea45dd9bbb4b39266b380af308ee4baa339d1))
* **api:** api update ([#523](https://github.com/conductor-is/conductor-python/issues/523)) ([e97b265](https://github.com/conductor-is/conductor-python/commit/e97b2657a8d0bb7883f80befdd350ac71cfdac64))
* **api:** api update ([#524](https://github.com/conductor-is/conductor-python/issues/524)) ([c307185](https://github.com/conductor-is/conductor-python/commit/c307185ee2bdce25efc7767482a60829b7a3a1c7))
* **api:** api update ([#525](https://github.com/conductor-is/conductor-python/issues/525)) ([bc1c277](https://github.com/conductor-is/conductor-python/commit/bc1c277b990663987e0076e8b31390fb1cc0d643))
* **api:** api update ([#526](https://github.com/conductor-is/conductor-python/issues/526)) ([bfa7493](https://github.com/conductor-is/conductor-python/commit/bfa7493d49f0b6155c60f634928820acea0f9a5d))

## 1.3.0 (2025-01-29)

Full Changelog: [v1.2.0...v1.3.0](https://github.com/conductor-is/conductor-python/compare/v1.2.0...v1.3.0)

### Features

* **api:** api update ([#515](https://github.com/conductor-is/conductor-python/issues/515)) ([5e1d047](https://github.com/conductor-is/conductor-python/commit/5e1d0475991aade9e5cffb9cff38b8210694d9e1))
* **api:** api update ([#518](https://github.com/conductor-is/conductor-python/issues/518)) ([9c00018](https://github.com/conductor-is/conductor-python/commit/9c00018a9027079cc41d60e12842f4d4b6d54bf0))


### Chores

* **internal:** codegen related update ([#517](https://github.com/conductor-is/conductor-python/issues/517)) ([60028f7](https://github.com/conductor-is/conductor-python/commit/60028f7b5e8b824a4682ce89b05720bcd1a1e4e6))

## 1.2.0 (2025-01-28)

Full Changelog: [v1.1.0...v1.2.0](https://github.com/conductor-is/conductor-python/compare/v1.1.0...v1.2.0)

### Features

* **api:** api update ([#512](https://github.com/conductor-is/conductor-python/issues/512)) ([9963580](https://github.com/conductor-is/conductor-python/commit/9963580f1324fcbe8c0d8a37345fa0351b98c6ae))

## 1.1.0 (2025-01-28)

Full Changelog: [v1.0.0...v1.1.0](https://github.com/conductor-is/conductor-python/compare/v1.0.0...v1.1.0)

### Features

* **api:** api update ([#504](https://github.com/conductor-is/conductor-python/issues/504)) ([7166baf](https://github.com/conductor-is/conductor-python/commit/7166baf69cdcc8f3889151b6ace2da0c7c9aa827))
* **api:** api update ([#505](https://github.com/conductor-is/conductor-python/issues/505)) ([440c033](https://github.com/conductor-is/conductor-python/commit/440c033f3be54d794f04fd641662eb55ab79a2f4))
* **api:** api update ([#506](https://github.com/conductor-is/conductor-python/issues/506)) ([b82740f](https://github.com/conductor-is/conductor-python/commit/b82740fde426378daa78b30cd49dcd4231c0c74c))
* **api:** api update ([#507](https://github.com/conductor-is/conductor-python/issues/507)) ([f02a06c](https://github.com/conductor-is/conductor-python/commit/f02a06cfde446a1e6438a66a602714c928dc0fc3))
* **api:** api update ([#508](https://github.com/conductor-is/conductor-python/issues/508)) ([1a14bba](https://github.com/conductor-is/conductor-python/commit/1a14bbabcf21d74942a670b550c31f3c69b4b0f3))
* **api:** api update ([#509](https://github.com/conductor-is/conductor-python/issues/509)) ([c2dfb27](https://github.com/conductor-is/conductor-python/commit/c2dfb277e3815edc648a9ca98c3e860295646a41))
* **api:** api update ([#510](https://github.com/conductor-is/conductor-python/issues/510)) ([5c6dae0](https://github.com/conductor-is/conductor-python/commit/5c6dae0a78856a97d748b5c64d81f77d783444f9))


### Chores

* **internal:** codegen related update ([#503](https://github.com/conductor-is/conductor-python/issues/503)) ([b7ce573](https://github.com/conductor-is/conductor-python/commit/b7ce573be57cda39d7010cde30e078f36cd848d7))
* remove custom code ([9e9acdb](https://github.com/conductor-is/conductor-python/commit/9e9acdb17d8dfac550b387e6577cfa01f3b99b53))

## 1.0.0 (2025-01-23)

Full Changelog: [v0.1.0-alpha.61...v1.0.0](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.61...v1.0.0)

### Features

* **api:** api update ([#495](https://github.com/conductor-is/conductor-python/issues/495)) ([9a02700](https://github.com/conductor-is/conductor-python/commit/9a02700619664502179f7ea4f3ca95e25fa49d3f))
* **api:** api update ([#497](https://github.com/conductor-is/conductor-python/issues/497)) ([54821a3](https://github.com/conductor-is/conductor-python/commit/54821a39a7f357f04377e41298240ce69bf3c157))
* **api:** api update ([#498](https://github.com/conductor-is/conductor-python/issues/498)) ([01179fe](https://github.com/conductor-is/conductor-python/commit/01179fee3ab395585a64caf86f3847a9a53afea5))
* **api:** api update ([#499](https://github.com/conductor-is/conductor-python/issues/499)) ([afec7aa](https://github.com/conductor-is/conductor-python/commit/afec7aa6661069c511331414666519931e300c01))
* **api:** api update ([#500](https://github.com/conductor-is/conductor-python/issues/500)) ([77e6d0d](https://github.com/conductor-is/conductor-python/commit/77e6d0dd71b5f2253e1d5946b754cc9a24e50413))

## 0.1.0-alpha.61 (2025-01-22)

Full Changelog: [v0.1.0-alpha.60...v0.1.0-alpha.61](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.60...v0.1.0-alpha.61)

### Features

* **api:** api update ([#486](https://github.com/conductor-is/conductor-python/issues/486)) ([60b6609](https://github.com/conductor-is/conductor-python/commit/60b6609d492f3eb6a444035ed074370a55073e13))
* **api:** api update ([#493](https://github.com/conductor-is/conductor-python/issues/493)) ([c4e9909](https://github.com/conductor-is/conductor-python/commit/c4e9909c74edc866f9702cf7c7bb92f92b807ff3))


### Bug Fixes

* **client:** only call .close() when needed ([#485](https://github.com/conductor-is/conductor-python/issues/485)) ([42798c9](https://github.com/conductor-is/conductor-python/commit/42798c91c6d5850412f41a2879b0ff81d3830223))
* correctly handle deserialising `cls` fields ([#488](https://github.com/conductor-is/conductor-python/issues/488)) ([ee0691d](https://github.com/conductor-is/conductor-python/commit/ee0691db61992c0a8afbadb11901705d136da9ab))


### Chores

* add missing isclass check ([#482](https://github.com/conductor-is/conductor-python/issues/482)) ([bb3eb6d](https://github.com/conductor-is/conductor-python/commit/bb3eb6df78222f6a963ffc5320992e115d15e4e5))
* **internal:** codegen related update ([#484](https://github.com/conductor-is/conductor-python/issues/484)) ([7ec3175](https://github.com/conductor-is/conductor-python/commit/7ec317567421ae46b1079377f21c9eec4fe07ea6))
* **internal:** codegen related update ([#487](https://github.com/conductor-is/conductor-python/issues/487)) ([d0cfe06](https://github.com/conductor-is/conductor-python/commit/d0cfe061b6f2420eef73caeacf5c7a8e84f0adba))
* **internal:** codegen related update ([#489](https://github.com/conductor-is/conductor-python/issues/489)) ([c183a5f](https://github.com/conductor-is/conductor-python/commit/c183a5f83e5dc9901a3c5e7a01541f9765006840))
* **internal:** codegen related update ([#490](https://github.com/conductor-is/conductor-python/issues/490)) ([23e92e3](https://github.com/conductor-is/conductor-python/commit/23e92e390237249b4320b8ee470e6e648ed3838c))
* **internal:** codegen related update ([#491](https://github.com/conductor-is/conductor-python/issues/491)) ([80b7535](https://github.com/conductor-is/conductor-python/commit/80b7535d978f026e9a35de981c5f44ea1c466539))
* **internal:** minor style changes ([#492](https://github.com/conductor-is/conductor-python/issues/492)) ([cbe4453](https://github.com/conductor-is/conductor-python/commit/cbe4453aeea2a4f9eeebaefc2eef611bfa14866f))

## 0.1.0-alpha.60 (2025-01-01)

Full Changelog: [v0.1.0-alpha.59...v0.1.0-alpha.60](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.59...v0.1.0-alpha.60)

### Features

* **api:** api update ([#477](https://github.com/conductor-is/conductor-python/issues/477)) ([f191f99](https://github.com/conductor-is/conductor-python/commit/f191f99e763e9024deca2d51291e90edbc340d38))
* **api:** api update ([#479](https://github.com/conductor-is/conductor-python/issues/479)) ([10b2b88](https://github.com/conductor-is/conductor-python/commit/10b2b88498f679bbe6b6fee888f23eb9bf2e017a))
* **api:** api update ([#480](https://github.com/conductor-is/conductor-python/issues/480)) ([c78ad18](https://github.com/conductor-is/conductor-python/commit/c78ad18c57b6805078a01e86efb8905874b87542))

## 0.1.0-alpha.59 (2024-12-31)

Full Changelog: [v0.1.0-alpha.58...v0.1.0-alpha.59](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.58...v0.1.0-alpha.59)

### Features

* **api:** api update ([#471](https://github.com/conductor-is/conductor-python/issues/471)) ([bd6a52e](https://github.com/conductor-is/conductor-python/commit/bd6a52e5cf41d231d081092ffa6837d594cbbc6a))
* **api:** api update ([#473](https://github.com/conductor-is/conductor-python/issues/473)) ([c9b061b](https://github.com/conductor-is/conductor-python/commit/c9b061ba1679ad6b7c6b5ffe31b37cc3adf452a2))
* **api:** api update ([#474](https://github.com/conductor-is/conductor-python/issues/474)) ([98cbbdf](https://github.com/conductor-is/conductor-python/commit/98cbbdf78ffa0b6da52fbc045f78ee8d5f02eb5c))
* **api:** manual updates ([#475](https://github.com/conductor-is/conductor-python/issues/475)) ([66bae2c](https://github.com/conductor-is/conductor-python/commit/66bae2c24992f4cfc0a76f25f265b48355bf7e9b))

## 0.1.0-alpha.58 (2024-12-30)

Full Changelog: [v0.1.0-alpha.57...v0.1.0-alpha.58](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.57...v0.1.0-alpha.58)

### Features

* **api:** api update ([#468](https://github.com/conductor-is/conductor-python/issues/468)) ([b09c409](https://github.com/conductor-is/conductor-python/commit/b09c40994f417a14ff677a54e5bb8a2e520d4748))
* **api:** api update ([#469](https://github.com/conductor-is/conductor-python/issues/469)) ([a85fed8](https://github.com/conductor-is/conductor-python/commit/a85fed89a29de99650e9fc038acaadef9cc0fd2d))
* **api:** manual updates ([#465](https://github.com/conductor-is/conductor-python/issues/465)) ([289c007](https://github.com/conductor-is/conductor-python/commit/289c007518327a8990632fc8525d404da817b19c))
* **api:** manual updates ([#467](https://github.com/conductor-is/conductor-python/issues/467)) ([5ff74b8](https://github.com/conductor-is/conductor-python/commit/5ff74b8ee0bd4be3eb4834ca2eefc14de3d24579))

## 0.1.0-alpha.57 (2024-12-29)

Full Changelog: [v0.1.0-alpha.56...v0.1.0-alpha.57](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.56...v0.1.0-alpha.57)

### Features

* **api:** api update ([#460](https://github.com/conductor-is/conductor-python/issues/460)) ([7726f0b](https://github.com/conductor-is/conductor-python/commit/7726f0b6282f19cbae0831b5e725df513b11a405))
* **api:** api update ([#462](https://github.com/conductor-is/conductor-python/issues/462)) ([ea117bb](https://github.com/conductor-is/conductor-python/commit/ea117bb50dde6fe65fac1e3a3c0c9d718f31550b))
* **api:** api update ([#463](https://github.com/conductor-is/conductor-python/issues/463)) ([c521f1d](https://github.com/conductor-is/conductor-python/commit/c521f1d103da4fc9b98b5baede7eef8f6d1dd81f))

## 0.1.0-alpha.56 (2024-12-27)

Full Changelog: [v0.1.0-alpha.55...v0.1.0-alpha.56](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.55...v0.1.0-alpha.56)

### Features

* **api:** api update ([#455](https://github.com/conductor-is/conductor-python/issues/455)) ([88417ca](https://github.com/conductor-is/conductor-python/commit/88417cae18adb2d6f335417705e1f2b0e14b2161))
* **api:** api update ([#457](https://github.com/conductor-is/conductor-python/issues/457)) ([313d8d2](https://github.com/conductor-is/conductor-python/commit/313d8d22b6045a3b276e519e5ed5154184a54af9))
* **api:** api update ([#458](https://github.com/conductor-is/conductor-python/issues/458)) ([2034b90](https://github.com/conductor-is/conductor-python/commit/2034b902e61f93ca13edbd8a83e921d1e7b99be0))

## 0.1.0-alpha.55 (2024-12-26)

Full Changelog: [v0.1.0-alpha.54...v0.1.0-alpha.55](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.54...v0.1.0-alpha.55)

### Features

* **api:** api update ([#441](https://github.com/conductor-is/conductor-python/issues/441)) ([ec2a50f](https://github.com/conductor-is/conductor-python/commit/ec2a50f1490e9d5a7fbc73dd646337d335194258))
* **api:** api update ([#443](https://github.com/conductor-is/conductor-python/issues/443)) ([1245a7e](https://github.com/conductor-is/conductor-python/commit/1245a7ec5de0ebda05dfb8af6c419a2d9cdf1688))
* **api:** api update ([#444](https://github.com/conductor-is/conductor-python/issues/444)) ([619916e](https://github.com/conductor-is/conductor-python/commit/619916e051a55a55f60719f96ff566bc3f9444a3))
* **api:** api update ([#445](https://github.com/conductor-is/conductor-python/issues/445)) ([1cfb5e4](https://github.com/conductor-is/conductor-python/commit/1cfb5e41a2deb6d6a5053e8d704d1be7c52bdc3b))
* **api:** api update ([#446](https://github.com/conductor-is/conductor-python/issues/446)) ([4884a14](https://github.com/conductor-is/conductor-python/commit/4884a14fcc0e864475083fa7db9f4831f8d231c5))
* **api:** api update ([#447](https://github.com/conductor-is/conductor-python/issues/447)) ([119b9ad](https://github.com/conductor-is/conductor-python/commit/119b9ada97ed946f3e87981bfa8b6a197fb698c8))
* **api:** api update ([#448](https://github.com/conductor-is/conductor-python/issues/448)) ([fe50670](https://github.com/conductor-is/conductor-python/commit/fe506704297497f6817a144255a4e8358a07643d))
* **api:** api update ([#449](https://github.com/conductor-is/conductor-python/issues/449)) ([11a1518](https://github.com/conductor-is/conductor-python/commit/11a1518d6f255c2abab49f5cdbb09b6fb942b688))
* **api:** api update ([#450](https://github.com/conductor-is/conductor-python/issues/450)) ([ef167b4](https://github.com/conductor-is/conductor-python/commit/ef167b4c6f82946adc662fc27a245d326edb499e))
* **api:** api update ([#451](https://github.com/conductor-is/conductor-python/issues/451)) ([07eb006](https://github.com/conductor-is/conductor-python/commit/07eb006c0dad55f9c1477e3682c6dd4415456d10))
* **api:** api update ([#452](https://github.com/conductor-is/conductor-python/issues/452)) ([8e221b4](https://github.com/conductor-is/conductor-python/commit/8e221b4a7486d0db472d74d715db98a9a1698e78))
* **api:** api update ([#453](https://github.com/conductor-is/conductor-python/issues/453)) ([22ded45](https://github.com/conductor-is/conductor-python/commit/22ded458ea5fb278533638850ad8376fc34a9059))

## 0.1.0-alpha.54 (2024-12-24)

Full Changelog: [v0.1.0-alpha.53...v0.1.0-alpha.54](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.53...v0.1.0-alpha.54)

### Features

* **api:** api update ([#436](https://github.com/conductor-is/conductor-python/issues/436)) ([08afef0](https://github.com/conductor-is/conductor-python/commit/08afef0b8a881f50d4de824fd53b934d607e2bb6))
* **api:** api update ([#438](https://github.com/conductor-is/conductor-python/issues/438)) ([a6c9f4e](https://github.com/conductor-is/conductor-python/commit/a6c9f4e47cd9c3265c740a14b879b0eb2dcedb61))
* **api:** api update ([#439](https://github.com/conductor-is/conductor-python/issues/439)) ([15d9a26](https://github.com/conductor-is/conductor-python/commit/15d9a266bd01766b721a3fef96bc13c5898098c4))

## 0.1.0-alpha.53 (2024-12-23)

Full Changelog: [v0.1.0-alpha.52...v0.1.0-alpha.53](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.52...v0.1.0-alpha.53)

### Features

* **api:** api update ([#427](https://github.com/conductor-is/conductor-python/issues/427)) ([19d01e1](https://github.com/conductor-is/conductor-python/commit/19d01e13266a8ba623caee6db01d061ccda10327))
* **api:** api update ([#432](https://github.com/conductor-is/conductor-python/issues/432)) ([d2fa31c](https://github.com/conductor-is/conductor-python/commit/d2fa31ca10bbe64cff053036e0c2b89136a3be7c))
* **api:** api update ([#433](https://github.com/conductor-is/conductor-python/issues/433)) ([9767e60](https://github.com/conductor-is/conductor-python/commit/9767e60acdf476ec83583ed306c60c3691208147))
* **api:** manual updates ([#423](https://github.com/conductor-is/conductor-python/issues/423)) ([4a705bf](https://github.com/conductor-is/conductor-python/commit/4a705bfeaa5c68b10fb73812e0aace1249f558c6))
* **api:** manual updates ([#425](https://github.com/conductor-is/conductor-python/issues/425)) ([3c72f87](https://github.com/conductor-is/conductor-python/commit/3c72f87a5cb1dfd3b04ac26b685953a53bb82a1f))
* **api:** manual updates ([#426](https://github.com/conductor-is/conductor-python/issues/426)) ([4956f07](https://github.com/conductor-is/conductor-python/commit/4956f0773a650ae040629484e30b046e2ca49d1f))
* **api:** manual updates ([#428](https://github.com/conductor-is/conductor-python/issues/428)) ([49ca345](https://github.com/conductor-is/conductor-python/commit/49ca34536b97e991e91f71e1399064a54ea7bdc2))
* **api:** manual updates ([#429](https://github.com/conductor-is/conductor-python/issues/429)) ([1e5752a](https://github.com/conductor-is/conductor-python/commit/1e5752a0f1066c4a02d91d5636139ab3f314b9d0))
* **api:** manual updates ([#430](https://github.com/conductor-is/conductor-python/issues/430)) ([c6e5f10](https://github.com/conductor-is/conductor-python/commit/c6e5f100e5cd9e53c1de229c3b91e486ab4f7a0a))
* **api:** manual updates ([#431](https://github.com/conductor-is/conductor-python/issues/431)) ([96977ec](https://github.com/conductor-is/conductor-python/commit/96977ec72d28e9e7f65faccabd33b0bafd58d22b))
* **api:** manual updates ([#434](https://github.com/conductor-is/conductor-python/issues/434)) ([98cb098](https://github.com/conductor-is/conductor-python/commit/98cb09884e7127d944806b5fb3aa29c1e794930d))

## 0.1.0-alpha.52 (2024-12-22)

Full Changelog: [v0.1.0-alpha.51...v0.1.0-alpha.52](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.51...v0.1.0-alpha.52)

### Features

* **api:** manual updates ([#420](https://github.com/conductor-is/conductor-python/issues/420)) ([9055522](https://github.com/conductor-is/conductor-python/commit/90555222bccab0db803ed8746e2b6c450a314236))

## 0.1.0-alpha.51 (2024-12-22)

Full Changelog: [v0.1.0-alpha.50...v0.1.0-alpha.51](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.50...v0.1.0-alpha.51)

### Features

* **api:** api update ([#414](https://github.com/conductor-is/conductor-python/issues/414)) ([ebd1a99](https://github.com/conductor-is/conductor-python/commit/ebd1a995906602b67c68a035537955835f25f6ea))
* **api:** api update ([#416](https://github.com/conductor-is/conductor-python/issues/416)) ([b431aac](https://github.com/conductor-is/conductor-python/commit/b431aac57cf96516a65369c4169362d5025d3abe))
* **api:** api update ([#417](https://github.com/conductor-is/conductor-python/issues/417)) ([d9e939c](https://github.com/conductor-is/conductor-python/commit/d9e939c8853b2484601ed4eba4ba8d678154779d))
* **api:** manual updates ([#412](https://github.com/conductor-is/conductor-python/issues/412)) ([145697f](https://github.com/conductor-is/conductor-python/commit/145697f8f20a053e6afdbdfcf049fdbf3eb103cd))
* **api:** manual updates ([#415](https://github.com/conductor-is/conductor-python/issues/415)) ([f823861](https://github.com/conductor-is/conductor-python/commit/f8238616af644f9cf3c6238cccc18d3cc154e3e1))
* **api:** manual updates ([#418](https://github.com/conductor-is/conductor-python/issues/418)) ([ee3ba19](https://github.com/conductor-is/conductor-python/commit/ee3ba1979c507ca88a28e8ac8a45d3755eaa840d))

## 0.1.0-alpha.50 (2024-12-21)

Full Changelog: [v0.1.0-alpha.49...v0.1.0-alpha.50](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.49...v0.1.0-alpha.50)

### Features

* **api:** api update ([#399](https://github.com/conductor-is/conductor-python/issues/399)) ([319a07d](https://github.com/conductor-is/conductor-python/commit/319a07da197f406960c22f3614efea67f37f5226))
* **api:** api update ([#406](https://github.com/conductor-is/conductor-python/issues/406)) ([e6a2a7b](https://github.com/conductor-is/conductor-python/commit/e6a2a7b719d54fd12df2e2c6d6a8175936f562d3))
* **api:** api update ([#407](https://github.com/conductor-is/conductor-python/issues/407)) ([b08b290](https://github.com/conductor-is/conductor-python/commit/b08b2908de6f9a2669ef1b1031c9b3bab2acf837))
* **api:** api update ([#408](https://github.com/conductor-is/conductor-python/issues/408)) ([72f3750](https://github.com/conductor-is/conductor-python/commit/72f37501ac91a730b710adf4c63a305f7d804fcf))
* **api:** api update ([#409](https://github.com/conductor-is/conductor-python/issues/409)) ([24e4f1c](https://github.com/conductor-is/conductor-python/commit/24e4f1c45ffb82ad7127660c5e29852dd27d0e02))
* **api:** manual updates ([#410](https://github.com/conductor-is/conductor-python/issues/410)) ([53459a9](https://github.com/conductor-is/conductor-python/commit/53459a93b1d7de3194835960a5ae76fe9f53e0ae))


### Chores

* **internal:** codegen related update ([#391](https://github.com/conductor-is/conductor-python/issues/391)) ([98a90b7](https://github.com/conductor-is/conductor-python/commit/98a90b791b4c068bc1a08c5bc25dc7e749d22877))
* **internal:** codegen related update ([#393](https://github.com/conductor-is/conductor-python/issues/393)) ([afc86f7](https://github.com/conductor-is/conductor-python/commit/afc86f70eda987bb3e5dbe7a70ac48b1d1669818))
* **internal:** codegen related update ([#394](https://github.com/conductor-is/conductor-python/issues/394)) ([94efe5c](https://github.com/conductor-is/conductor-python/commit/94efe5c020dc78148436afbaf676963c1405884b))
* **internal:** codegen related update ([#395](https://github.com/conductor-is/conductor-python/issues/395)) ([ae3c6cf](https://github.com/conductor-is/conductor-python/commit/ae3c6cf783f7e0a80c486dab1cd282ff10314a70))
* **internal:** codegen related update ([#396](https://github.com/conductor-is/conductor-python/issues/396)) ([5e9098b](https://github.com/conductor-is/conductor-python/commit/5e9098bf62cbfba3f1bc0c038464397c5bbe86d0))
* **internal:** codegen related update ([#397](https://github.com/conductor-is/conductor-python/issues/397)) ([f71f2ee](https://github.com/conductor-is/conductor-python/commit/f71f2eefb20b317c61468337e0bfe03e27cd9ec8))
* **internal:** codegen related update ([#398](https://github.com/conductor-is/conductor-python/issues/398)) ([5f13d01](https://github.com/conductor-is/conductor-python/commit/5f13d018b88fa23628073c15e8c35713700a564a))
* **internal:** codegen related update ([#401](https://github.com/conductor-is/conductor-python/issues/401)) ([9e18c7f](https://github.com/conductor-is/conductor-python/commit/9e18c7fc9d1cc5cec02b5eca0554d7d61ff7ed90))
* **internal:** codegen related update ([#402](https://github.com/conductor-is/conductor-python/issues/402)) ([7c0aaf9](https://github.com/conductor-is/conductor-python/commit/7c0aaf947a4d7a6051a5d9f0e1aff91a2b75a131))
* **internal:** codegen related update ([#403](https://github.com/conductor-is/conductor-python/issues/403)) ([0db495f](https://github.com/conductor-is/conductor-python/commit/0db495f0937e03c938c87781c5a16d07142496ce))
* **internal:** codegen related update ([#404](https://github.com/conductor-is/conductor-python/issues/404)) ([5a6f82f](https://github.com/conductor-is/conductor-python/commit/5a6f82fe7d31b5b0f4675737b01dbc28c2128125))
* **internal:** fix some typos ([#405](https://github.com/conductor-is/conductor-python/issues/405)) ([bae2c8d](https://github.com/conductor-is/conductor-python/commit/bae2c8d7fdb49d256e08db1ce132e9ed86934b88))

## 0.1.0-alpha.49 (2024-12-18)

Full Changelog: [v0.1.0-alpha.48...v0.1.0-alpha.49](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.48...v0.1.0-alpha.49)

### Features

* **api:** api update ([#386](https://github.com/conductor-is/conductor-python/issues/386)) ([af91c2d](https://github.com/conductor-is/conductor-python/commit/af91c2d0b3ffb83e447fb5b5f0fc2dfcc0d9e086))
* **api:** manual updates ([#388](https://github.com/conductor-is/conductor-python/issues/388)) ([44ad617](https://github.com/conductor-is/conductor-python/commit/44ad617bc86b1b601f966d0d6e8fce265fb5a9a8))
* **api:** manual updates ([#389](https://github.com/conductor-is/conductor-python/issues/389)) ([68f725f](https://github.com/conductor-is/conductor-python/commit/68f725f780b7ad599b9ec81298d27f3c2a4ac010))

## 0.1.0-alpha.48 (2024-12-17)

Full Changelog: [v0.1.0-alpha.47...v0.1.0-alpha.48](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.47...v0.1.0-alpha.48)

### Features

* **api:** api update ([#376](https://github.com/conductor-is/conductor-python/issues/376)) ([bce766c](https://github.com/conductor-is/conductor-python/commit/bce766c2d0629839cc87a3d0280a1f2fe9171700))
* **api:** manual updates ([#380](https://github.com/conductor-is/conductor-python/issues/380)) ([e3b1208](https://github.com/conductor-is/conductor-python/commit/e3b1208a60bfbf5f33291efa3657a4e7b62e9832))
* **api:** manual updates ([#381](https://github.com/conductor-is/conductor-python/issues/381)) ([cd5cc52](https://github.com/conductor-is/conductor-python/commit/cd5cc52a31fa317013cc4d6e09e71f1281d9887d))
* **api:** manual updates ([#382](https://github.com/conductor-is/conductor-python/issues/382)) ([728c2fc](https://github.com/conductor-is/conductor-python/commit/728c2fcb1981aa5cc959288cc27fcc77e1bcdab2))
* **api:** manual updates ([#383](https://github.com/conductor-is/conductor-python/issues/383)) ([08a2025](https://github.com/conductor-is/conductor-python/commit/08a2025a7e1756465bf0439e0a0f57cdb4745538))
* **api:** manual updates ([#384](https://github.com/conductor-is/conductor-python/issues/384)) ([cc43d75](https://github.com/conductor-is/conductor-python/commit/cc43d75a052d5af3fce21a1eea8033efac3d6a3f))


### Chores

* **internal:** codegen related update ([#379](https://github.com/conductor-is/conductor-python/issues/379)) ([62bf29a](https://github.com/conductor-is/conductor-python/commit/62bf29a352b868450c70f49b20b26755a87126f9))

## 0.1.0-alpha.47 (2024-12-11)

Full Changelog: [v0.1.0-alpha.46...v0.1.0-alpha.47](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.46...v0.1.0-alpha.47)

### Features

* **api:** api update ([#374](https://github.com/conductor-is/conductor-python/issues/374)) ([b3879c3](https://github.com/conductor-is/conductor-python/commit/b3879c35001adc1802a4629f6af8f38b8bcc6670))


### Chores

* **internal:** codegen related update ([#372](https://github.com/conductor-is/conductor-python/issues/372)) ([ef1cb95](https://github.com/conductor-is/conductor-python/commit/ef1cb95433acfa60037026cfe531849c78e45930))

## 0.1.0-alpha.46 (2024-12-10)

Full Changelog: [v0.1.0-alpha.45...v0.1.0-alpha.46](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.45...v0.1.0-alpha.46)

### Features

* **api:** api update ([#367](https://github.com/conductor-is/conductor-python/issues/367)) ([0906a44](https://github.com/conductor-is/conductor-python/commit/0906a44f297b20a8679390108455c7fd262ffe76))
* **api:** api update ([#369](https://github.com/conductor-is/conductor-python/issues/369)) ([41ddd81](https://github.com/conductor-is/conductor-python/commit/41ddd81fa5ac292d0ba357ef950a51ce06951582))
* **api:** api update ([#370](https://github.com/conductor-is/conductor-python/issues/370)) ([5d46b06](https://github.com/conductor-is/conductor-python/commit/5d46b0674b6b3ff69b4f0cc226434f9b3f9fabe7))

## 0.1.0-alpha.45 (2024-12-09)

Full Changelog: [v0.1.0-alpha.44...v0.1.0-alpha.45](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.44...v0.1.0-alpha.45)

### Features

* **api:** api update ([#362](https://github.com/conductor-is/conductor-python/issues/362)) ([195340a](https://github.com/conductor-is/conductor-python/commit/195340a1aa5a709e10fc46c07a2c047075719f7e))
* **api:** api update ([#364](https://github.com/conductor-is/conductor-python/issues/364)) ([3905426](https://github.com/conductor-is/conductor-python/commit/3905426e5e7319bdaec9cfb7bf245239f43f3778))
* **api:** api update ([#365](https://github.com/conductor-is/conductor-python/issues/365)) ([54330cc](https://github.com/conductor-is/conductor-python/commit/54330ccc97371f921a104b14e23d45cc115fe69e))

## 0.1.0-alpha.44 (2024-12-08)

Full Changelog: [v0.1.0-alpha.43...v0.1.0-alpha.44](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.43...v0.1.0-alpha.44)

### Features

* **api:** api update ([#354](https://github.com/conductor-is/conductor-python/issues/354)) ([bdb3213](https://github.com/conductor-is/conductor-python/commit/bdb3213aeaf78693c7c6a7a1f41c1ac0abb22e5c))
* **api:** api update ([#356](https://github.com/conductor-is/conductor-python/issues/356)) ([319db26](https://github.com/conductor-is/conductor-python/commit/319db26b70719f1709377a57081ff7ac77cf2cc4))
* **api:** api update ([#358](https://github.com/conductor-is/conductor-python/issues/358)) ([b80bfd7](https://github.com/conductor-is/conductor-python/commit/b80bfd7ceee58d0acdc2e8103f76ac2c4e5a3c6f))
* **api:** api update ([#359](https://github.com/conductor-is/conductor-python/issues/359)) ([b4dd522](https://github.com/conductor-is/conductor-python/commit/b4dd522b656b0640c262621ea1e914912b21c469))
* **api:** manual updates ([#357](https://github.com/conductor-is/conductor-python/issues/357)) ([ca098f1](https://github.com/conductor-is/conductor-python/commit/ca098f15ea02cee9f96aa01e52d28848caafb262))


### Bug Fixes

* **api:** rename bill payment endpoints ([#360](https://github.com/conductor-is/conductor-python/issues/360)) ([abe1a69](https://github.com/conductor-is/conductor-python/commit/abe1a69d0ad60a8ea03ad3c40076d07f255861b8))

## 0.1.0-alpha.43 (2024-12-05)

Full Changelog: [v0.1.0-alpha.42...v0.1.0-alpha.43](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.42...v0.1.0-alpha.43)

### Features

* **api:** api update ([#344](https://github.com/conductor-is/conductor-python/issues/344)) ([c8130ca](https://github.com/conductor-is/conductor-python/commit/c8130ca105328e54ab132660ec72db746e04e81a))
* **api:** api update ([#345](https://github.com/conductor-is/conductor-python/issues/345)) ([1a7155e](https://github.com/conductor-is/conductor-python/commit/1a7155ea2a428aed74204f099d2be3fadfb1b181))
* **api:** api update ([#347](https://github.com/conductor-is/conductor-python/issues/347)) ([fc1936a](https://github.com/conductor-is/conductor-python/commit/fc1936a9fb4fbc5e0d228b2dd51391e03a7916f3))
* **api:** api update ([#348](https://github.com/conductor-is/conductor-python/issues/348)) ([021deda](https://github.com/conductor-is/conductor-python/commit/021dedacddd82e494e19f0139d2fcf79c5cd8e9f))
* **api:** api update ([#350](https://github.com/conductor-is/conductor-python/issues/350)) ([d0a88ac](https://github.com/conductor-is/conductor-python/commit/d0a88acf951b18d4f3d37fe993dd923d76d74b3e))
* **api:** api update ([#351](https://github.com/conductor-is/conductor-python/issues/351)) ([d05ad21](https://github.com/conductor-is/conductor-python/commit/d05ad218007d93586ac4b029d363731a30fdf42b))
* **api:** manual updates ([#346](https://github.com/conductor-is/conductor-python/issues/346)) ([dc47c24](https://github.com/conductor-is/conductor-python/commit/dc47c24bbbccedf323f8256e53e611821a50decd))
* **api:** manual updates ([#349](https://github.com/conductor-is/conductor-python/issues/349)) ([9b24566](https://github.com/conductor-is/conductor-python/commit/9b24566fdc13d42e2fe64489877492641da68644))


### Bug Fixes

* class member name when assigning an aliased class member to a variable ([#352](https://github.com/conductor-is/conductor-python/issues/352)) ([6d64aea](https://github.com/conductor-is/conductor-python/commit/6d64aead8abf19b73141daec0a353728f77276b6))
* **client:** compat with new httpx 0.28.0 release ([#340](https://github.com/conductor-is/conductor-python/issues/340)) ([6284bae](https://github.com/conductor-is/conductor-python/commit/6284bae815d3edf486c329df7f9eddc3a7506270))


### Chores

* **internal:** bump pyright ([#342](https://github.com/conductor-is/conductor-python/issues/342)) ([c7009ef](https://github.com/conductor-is/conductor-python/commit/c7009ef01f37a58ff61c60aad1aa2fd2a94afbf3))
* **internal:** codegen related update ([#341](https://github.com/conductor-is/conductor-python/issues/341)) ([f200bd6](https://github.com/conductor-is/conductor-python/commit/f200bd60624333847a3cfd73901faeb8cdd6f3e0))
* **internal:** exclude mypy from running on tests ([#338](https://github.com/conductor-is/conductor-python/issues/338)) ([da09201](https://github.com/conductor-is/conductor-python/commit/da092012888f76eb49181385afc2f1d590b7a335))
* make the `Omit` type public ([#343](https://github.com/conductor-is/conductor-python/issues/343)) ([1d2b41f](https://github.com/conductor-is/conductor-python/commit/1d2b41f49db44f666b1713fcd9744fe0f4eb00bc))

## 0.1.0-alpha.42 (2024-11-28)

Full Changelog: [v0.1.0-alpha.41...v0.1.0-alpha.42](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.41...v0.1.0-alpha.42)

### Features

* **api:** api update ([#334](https://github.com/conductor-is/conductor-python/issues/334)) ([59360a0](https://github.com/conductor-is/conductor-python/commit/59360a05645fd0ec3a7293a0b9e2f5cf33484396))
* **api:** api update ([#336](https://github.com/conductor-is/conductor-python/issues/336)) ([f3a9a2d](https://github.com/conductor-is/conductor-python/commit/f3a9a2dfb1be748db2ba2ef1d7ae2e550438c79f))

## 0.1.0-alpha.41 (2024-11-27)

Full Changelog: [v0.1.0-alpha.40...v0.1.0-alpha.41](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.40...v0.1.0-alpha.41)

### Features

* **api:** api update ([#324](https://github.com/conductor-is/conductor-python/issues/324)) ([5880f1b](https://github.com/conductor-is/conductor-python/commit/5880f1bf4a7ae045e43c7dacaf86742dff6face8))
* **api:** api update ([#326](https://github.com/conductor-is/conductor-python/issues/326)) ([5a77814](https://github.com/conductor-is/conductor-python/commit/5a77814a1928db788c7276da9a075ceb86340aa4))
* **api:** api update ([#327](https://github.com/conductor-is/conductor-python/issues/327)) ([5c709df](https://github.com/conductor-is/conductor-python/commit/5c709df4335c51160798e216920dac909212cfab))
* **api:** api update ([#330](https://github.com/conductor-is/conductor-python/issues/330)) ([4437162](https://github.com/conductor-is/conductor-python/commit/44371625dcf57acc8d431b4a6be36644a5e05f4a))
* **api:** api update ([#331](https://github.com/conductor-is/conductor-python/issues/331)) ([0791a12](https://github.com/conductor-is/conductor-python/commit/0791a1245b219a7ddaaa2dab6442f98ebc3c4809))
* **api:** api update ([#332](https://github.com/conductor-is/conductor-python/issues/332)) ([6255a42](https://github.com/conductor-is/conductor-python/commit/6255a4215fcfd2d97ba106346d578a2ea0976a0c))


### Chores

* remove now unused `cached-property` dep ([#329](https://github.com/conductor-is/conductor-python/issues/329)) ([49cd1a9](https://github.com/conductor-is/conductor-python/commit/49cd1a9ee29514366dc9c31f974a075f02bd3207))


### Documentation

* add info log level to readme ([#328](https://github.com/conductor-is/conductor-python/issues/328)) ([938fe94](https://github.com/conductor-is/conductor-python/commit/938fe948b8f8206dceff5504c71c9de08be6ea38))

## 0.1.0-alpha.40 (2024-11-22)

Full Changelog: [v0.1.0-alpha.39...v0.1.0-alpha.40](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.39...v0.1.0-alpha.40)

### Features

* **api:** api update ([#320](https://github.com/conductor-is/conductor-python/issues/320)) ([6f94372](https://github.com/conductor-is/conductor-python/commit/6f94372956f93f365d8902a8e27c35db2d7adb15))
* **api:** api update ([#322](https://github.com/conductor-is/conductor-python/issues/322)) ([322a528](https://github.com/conductor-is/conductor-python/commit/322a528d994b18ca07f22db4f0625f021ba3da0c))

## 0.1.0-alpha.39 (2024-11-22)

Full Changelog: [v0.1.0-alpha.38...v0.1.0-alpha.39](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.38...v0.1.0-alpha.39)

### Features

* **api:** api update ([#318](https://github.com/conductor-is/conductor-python/issues/318)) ([5e889b7](https://github.com/conductor-is/conductor-python/commit/5e889b7455340941804f0c2c0a4d83e43edb5841))


### Chores

* **internal:** fix compat model_dump method when warnings are passed ([#316](https://github.com/conductor-is/conductor-python/issues/316)) ([41bf269](https://github.com/conductor-is/conductor-python/commit/41bf269f99c5b036337e00176218920d88a9c850))

## 0.1.0-alpha.38 (2024-11-22)

Full Changelog: [v0.1.0-alpha.37...v0.1.0-alpha.38](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.37...v0.1.0-alpha.38)

### Features

* **api:** api update ([#313](https://github.com/conductor-is/conductor-python/issues/313)) ([7715330](https://github.com/conductor-is/conductor-python/commit/771533040af692733227179b45b69b0fefc6bca0))

## 0.1.0-alpha.37 (2024-11-22)

Full Changelog: [v0.1.0-alpha.36...v0.1.0-alpha.37](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.36...v0.1.0-alpha.37)

### Features

* **api:** api update ([#307](https://github.com/conductor-is/conductor-python/issues/307)) ([66afe6e](https://github.com/conductor-is/conductor-python/commit/66afe6e0a5a441dcecdbc6e819e93239d4a20725))
* **api:** api update ([#310](https://github.com/conductor-is/conductor-python/issues/310)) ([b34f9b0](https://github.com/conductor-is/conductor-python/commit/b34f9b0ac9c2f3dedee26ea20e042d44def7c15f))
* **api:** api update ([#311](https://github.com/conductor-is/conductor-python/issues/311)) ([14097ed](https://github.com/conductor-is/conductor-python/commit/14097edb9a25ea18540306c01f889828ba2303d6))


### Chores

* rebuild project due to codegen change ([#309](https://github.com/conductor-is/conductor-python/issues/309)) ([d7a932d](https://github.com/conductor-is/conductor-python/commit/d7a932d06403c0fdacd6a47cb6f9475c29d4c0f1))

## 0.1.0-alpha.36 (2024-11-17)

Full Changelog: [v0.1.0-alpha.35...v0.1.0-alpha.36](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.35...v0.1.0-alpha.36)

### Features

* **api:** api update ([#303](https://github.com/conductor-is/conductor-python/issues/303)) ([fb72473](https://github.com/conductor-is/conductor-python/commit/fb72473d9be51e41785acec48c5e1a293b0f4643))
* **api:** api update ([#305](https://github.com/conductor-is/conductor-python/issues/305)) ([07104f2](https://github.com/conductor-is/conductor-python/commit/07104f2383a6c7a67270651e42273394629cfaa5))
* **api:** api update ([#306](https://github.com/conductor-is/conductor-python/issues/306)) ([3016465](https://github.com/conductor-is/conductor-python/commit/301646549a68c9f325eed3dca56ae1ce9a88aed3))

## 0.1.0-alpha.35 (2024-11-17)

Full Changelog: [v0.1.0-alpha.34...v0.1.0-alpha.35](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.34...v0.1.0-alpha.35)

### Features

* **api:** api update ([#294](https://github.com/conductor-is/conductor-python/issues/294)) ([3f10892](https://github.com/conductor-is/conductor-python/commit/3f1089254a6680b1b0ee1f2aa0f53035efdb3872))
* **api:** api update ([#296](https://github.com/conductor-is/conductor-python/issues/296)) ([35bd17e](https://github.com/conductor-is/conductor-python/commit/35bd17e13b0e6f9a0bd6e92dc356da74f000e0f8))
* **api:** api update ([#297](https://github.com/conductor-is/conductor-python/issues/297)) ([1765972](https://github.com/conductor-is/conductor-python/commit/17659721ae55807c4ea1b134922d97f87e0409e7))
* **api:** api update ([#298](https://github.com/conductor-is/conductor-python/issues/298)) ([26b888b](https://github.com/conductor-is/conductor-python/commit/26b888bf5fdf0cee5e0463a0103e252fd98dd4e0))
* **api:** api update ([#299](https://github.com/conductor-is/conductor-python/issues/299)) ([26235d6](https://github.com/conductor-is/conductor-python/commit/26235d6a87abaf96f2d6347d4013d7884b106218))
* **api:** api update ([#300](https://github.com/conductor-is/conductor-python/issues/300)) ([9934816](https://github.com/conductor-is/conductor-python/commit/9934816306db035c00aac725f21011f385b78e84))
* **api:** manual updates ([#301](https://github.com/conductor-is/conductor-python/issues/301)) ([4a61f9c](https://github.com/conductor-is/conductor-python/commit/4a61f9cf932f632766f2590029f9a35669e3bad8))

## 0.1.0-alpha.34 (2024-11-14)

Full Changelog: [v0.1.0-alpha.33...v0.1.0-alpha.34](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.33...v0.1.0-alpha.34)

### Features

* **api:** api update ([#287](https://github.com/conductor-is/conductor-python/issues/287)) ([da64f61](https://github.com/conductor-is/conductor-python/commit/da64f613d07d596abd5e3ba0d3d2a0e0f5c40c79))
* **api:** api update ([#289](https://github.com/conductor-is/conductor-python/issues/289)) ([c6f58e7](https://github.com/conductor-is/conductor-python/commit/c6f58e78ff81a2816c73717493af1849008b70cb))
* **api:** api update ([#290](https://github.com/conductor-is/conductor-python/issues/290)) ([0a34b7a](https://github.com/conductor-is/conductor-python/commit/0a34b7a2aa974f504ea65ab19992440505789ede))
* **api:** api update ([#291](https://github.com/conductor-is/conductor-python/issues/291)) ([e371300](https://github.com/conductor-is/conductor-python/commit/e3713007f4f90e6b51385ed94b57877f864ace59))


### Styles

* **api:** reorder props ([#292](https://github.com/conductor-is/conductor-python/issues/292)) ([fbb2119](https://github.com/conductor-is/conductor-python/commit/fbb2119b07d0578518298a6bf1f752540484a276))

## 0.1.0-alpha.33 (2024-11-13)

Full Changelog: [v0.1.0-alpha.32...v0.1.0-alpha.33](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.32...v0.1.0-alpha.33)

### Features

* **api:** api update ([#280](https://github.com/conductor-is/conductor-python/issues/280)) ([99817d4](https://github.com/conductor-is/conductor-python/commit/99817d4b420146425304f46ddcd6277543fea64a))
* **api:** api update ([#282](https://github.com/conductor-is/conductor-python/issues/282)) ([4915327](https://github.com/conductor-is/conductor-python/commit/49153277d9a1e9c77ae5c723c8e9c9d5da4f56ff))
* **api:** api update ([#283](https://github.com/conductor-is/conductor-python/issues/283)) ([3f83852](https://github.com/conductor-is/conductor-python/commit/3f83852c3d6b54cbaddae4993c4c30c8d39ee105))
* **api:** api update ([#284](https://github.com/conductor-is/conductor-python/issues/284)) ([2809946](https://github.com/conductor-is/conductor-python/commit/2809946a1bce219eecc73677db5490e5151eee8b))
* **api:** api update ([#285](https://github.com/conductor-is/conductor-python/issues/285)) ([23c24f7](https://github.com/conductor-is/conductor-python/commit/23c24f7526bf11f7cc7d8bfaf1debf2cb848480f))

## 0.1.0-alpha.32 (2024-11-13)

Full Changelog: [v0.1.0-alpha.31...v0.1.0-alpha.32](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.31...v0.1.0-alpha.32)

### Styles

* **api:** reorder resource and method keys in config ([#277](https://github.com/conductor-is/conductor-python/issues/277)) ([45afd70](https://github.com/conductor-is/conductor-python/commit/45afd70fc57e03401cb0b2c9cd505823bc18dac1))

## 0.1.0-alpha.31 (2024-11-13)

Full Changelog: [v0.1.0-alpha.30...v0.1.0-alpha.31](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.30...v0.1.0-alpha.31)

### Features

* **api:** api update ([#274](https://github.com/conductor-is/conductor-python/issues/274)) ([7c8a091](https://github.com/conductor-is/conductor-python/commit/7c8a091ef86fb7566930ffcfe3059b7fedeec9bd))

## 0.1.0-alpha.30 (2024-11-13)

Full Changelog: [v0.1.0-alpha.29...v0.1.0-alpha.30](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.29...v0.1.0-alpha.30)

### Features

* **api:** api update ([#252](https://github.com/conductor-is/conductor-python/issues/252)) ([11c9b2e](https://github.com/conductor-is/conductor-python/commit/11c9b2ecf0d31d0dce305414452dd2d1a93b92b6))
* **api:** api update ([#253](https://github.com/conductor-is/conductor-python/issues/253)) ([56795a6](https://github.com/conductor-is/conductor-python/commit/56795a63212b51a1740b1476af5517fff7af0227))
* **api:** api update ([#254](https://github.com/conductor-is/conductor-python/issues/254)) ([d38487d](https://github.com/conductor-is/conductor-python/commit/d38487dbc0d56c3fb99d50a1789b6add73479c81))
* **api:** api update ([#255](https://github.com/conductor-is/conductor-python/issues/255)) ([29b6c46](https://github.com/conductor-is/conductor-python/commit/29b6c46815baca4d89d788b5cd141849e53024e9))
* **api:** api update ([#256](https://github.com/conductor-is/conductor-python/issues/256)) ([6a976f3](https://github.com/conductor-is/conductor-python/commit/6a976f35361f9e0f7e76397be26f65f83f4ff818))
* **api:** api update ([#258](https://github.com/conductor-is/conductor-python/issues/258)) ([4b20a25](https://github.com/conductor-is/conductor-python/commit/4b20a25cf5726726dea00746669a180da69c2308))
* **api:** api update ([#259](https://github.com/conductor-is/conductor-python/issues/259)) ([0c54a19](https://github.com/conductor-is/conductor-python/commit/0c54a19858d1144d5029b0055a099ac6bf1d9f34))
* **api:** api update ([#261](https://github.com/conductor-is/conductor-python/issues/261)) ([cd6abe3](https://github.com/conductor-is/conductor-python/commit/cd6abe3a48a8af3bb81f39ea476cf80c888ec119))
* **api:** api update ([#262](https://github.com/conductor-is/conductor-python/issues/262)) ([3da684c](https://github.com/conductor-is/conductor-python/commit/3da684c41751d12fc321a8050095aa1403df46c7))
* **api:** api update ([#263](https://github.com/conductor-is/conductor-python/issues/263)) ([877cceb](https://github.com/conductor-is/conductor-python/commit/877ccebe4e9e0a550bc8c76e6cccd44480bad7c9))
* **api:** api update ([#264](https://github.com/conductor-is/conductor-python/issues/264)) ([1cba4c9](https://github.com/conductor-is/conductor-python/commit/1cba4c9333440c0bdfc7f98a8b27010e7eee6231))
* **api:** api update ([#265](https://github.com/conductor-is/conductor-python/issues/265)) ([47f840d](https://github.com/conductor-is/conductor-python/commit/47f840d5f762b0cd065f7ea49182e73c74294297))
* **api:** api update ([#266](https://github.com/conductor-is/conductor-python/issues/266)) ([d724371](https://github.com/conductor-is/conductor-python/commit/d724371a7b10006750fa8fdf66ec32b07909bba3))
* **api:** api update ([#267](https://github.com/conductor-is/conductor-python/issues/267)) ([fb907df](https://github.com/conductor-is/conductor-python/commit/fb907df98b657b5f3e077355a632268b53fe3bc3))
* **api:** api update ([#268](https://github.com/conductor-is/conductor-python/issues/268)) ([5d6dd29](https://github.com/conductor-is/conductor-python/commit/5d6dd29ddaea2c4f58cb19f38f9b2dbfb960e8f3))
* **api:** api update ([#269](https://github.com/conductor-is/conductor-python/issues/269)) ([a564380](https://github.com/conductor-is/conductor-python/commit/a56438021b71c69cabfbcd9cf37fe40d0816e9e4))
* **api:** api update ([#270](https://github.com/conductor-is/conductor-python/issues/270)) ([c3664b0](https://github.com/conductor-is/conductor-python/commit/c3664b0bfd7b5e4d5cfb90d8205633bf3ec58e48))
* **api:** api update ([#272](https://github.com/conductor-is/conductor-python/issues/272)) ([7321711](https://github.com/conductor-is/conductor-python/commit/7321711ebbcae657a2d0f6ff67886c45ea9638bf))


### Chores

* rebuild project due to codegen change ([#250](https://github.com/conductor-is/conductor-python/issues/250)) ([ac2690e](https://github.com/conductor-is/conductor-python/commit/ac2690e8c1d35a931365cf4dcd5d6a25d6ad917a))
* rebuild project due to codegen change ([#257](https://github.com/conductor-is/conductor-python/issues/257)) ([b45caaa](https://github.com/conductor-is/conductor-python/commit/b45caaa2d2471df36b56d4b31140d33edf7d51bd))
* rebuild project due to codegen change ([#260](https://github.com/conductor-is/conductor-python/issues/260)) ([fa457e0](https://github.com/conductor-is/conductor-python/commit/fa457e01cec6d9c5aa98d59c7e06c55296b005ff))

## 0.1.0-alpha.29 (2024-11-11)

Full Changelog: [v0.1.0-alpha.28...v0.1.0-alpha.29](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.28...v0.1.0-alpha.29)

### Features

* **api:** api update ([#246](https://github.com/conductor-is/conductor-python/issues/246)) ([a3821f7](https://github.com/conductor-is/conductor-python/commit/a3821f7cdb5ec01a8dd57e3f5fcdf9885ef2fca5))


### Chores

* rebuild project due to codegen change ([#248](https://github.com/conductor-is/conductor-python/issues/248)) ([bd96d6a](https://github.com/conductor-is/conductor-python/commit/bd96d6abe924bc614bf20260692b3a907cf8e8c0))

## 0.1.0-alpha.28 (2024-11-08)

Full Changelog: [v0.1.0-alpha.27...v0.1.0-alpha.28](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.27...v0.1.0-alpha.28)

### Features

* **api:** api update ([#241](https://github.com/conductor-is/conductor-python/issues/241)) ([bd8bf90](https://github.com/conductor-is/conductor-python/commit/bd8bf904dd111630152172979725673df3668992))
* **api:** api update ([#244](https://github.com/conductor-is/conductor-python/issues/244)) ([5981b44](https://github.com/conductor-is/conductor-python/commit/5981b44b69d19e672ee77c8dd023f55115e2254c))


### Chores

* rebuild project due to codegen change ([#243](https://github.com/conductor-is/conductor-python/issues/243)) ([33b9a3d](https://github.com/conductor-is/conductor-python/commit/33b9a3daaa275a957f3fbd1a8d5215844a52b2f1))

## 0.1.0-alpha.27 (2024-11-05)

Full Changelog: [v0.1.0-alpha.26...v0.1.0-alpha.27](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.26...v0.1.0-alpha.27)

### Features

* **api:** api update ([#230](https://github.com/conductor-is/conductor-python/issues/230)) ([e339794](https://github.com/conductor-is/conductor-python/commit/e339794d5e43d47a259463ab86c28db1bbe03744))
* **api:** api update ([#232](https://github.com/conductor-is/conductor-python/issues/232)) ([66adc05](https://github.com/conductor-is/conductor-python/commit/66adc0587d8f0b3665153aaef75a0662dbea7d8c))
* **api:** api update ([#233](https://github.com/conductor-is/conductor-python/issues/233)) ([96d6201](https://github.com/conductor-is/conductor-python/commit/96d62011782a65db5747c43adba52b9b1d369e3b))
* **api:** api update ([#234](https://github.com/conductor-is/conductor-python/issues/234)) ([518f06a](https://github.com/conductor-is/conductor-python/commit/518f06ac0bf0c4f0b0d06bde7a73f412bd16010e))
* **api:** api update ([#236](https://github.com/conductor-is/conductor-python/issues/236)) ([cf93450](https://github.com/conductor-is/conductor-python/commit/cf934502b6c9ab26ade073191d55a7075408693d))
* **api:** api update ([#237](https://github.com/conductor-is/conductor-python/issues/237)) ([e808673](https://github.com/conductor-is/conductor-python/commit/e808673c7b00ef401a66677e9343132bd7fc4c6f))
* **api:** api update ([#239](https://github.com/conductor-is/conductor-python/issues/239)) ([1b8d8e8](https://github.com/conductor-is/conductor-python/commit/1b8d8e8325fa78d8b72f91addfae1ecb2ca247c2))
* **api:** manual updates ([#235](https://github.com/conductor-is/conductor-python/issues/235)) ([84b7a95](https://github.com/conductor-is/conductor-python/commit/84b7a954fd1575d9c46fb1886d4b68f310f71796))


### Refactors

* **api:** Fix check model name ([#238](https://github.com/conductor-is/conductor-python/issues/238)) ([d561a8b](https://github.com/conductor-is/conductor-python/commit/d561a8b9d5572370d8e46d91d9f5df57936d0164))

## 0.1.0-alpha.26 (2024-11-04)

Full Changelog: [v0.1.0-alpha.25...v0.1.0-alpha.26](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.25...v0.1.0-alpha.26)

### Features

* **api:** api update ([#221](https://github.com/conductor-is/conductor-python/issues/221)) ([d93e2e4](https://github.com/conductor-is/conductor-python/commit/d93e2e492dc317399c9dcf3c741bf111dbb3f1ab))
* **api:** api update ([#223](https://github.com/conductor-is/conductor-python/issues/223)) ([4c0ba46](https://github.com/conductor-is/conductor-python/commit/4c0ba46f2a933bcd33e0c0cd6291a4e59da5439a))
* **api:** api update ([#224](https://github.com/conductor-is/conductor-python/issues/224)) ([706ca7e](https://github.com/conductor-is/conductor-python/commit/706ca7e29a6d5e5f0f23a375cbc3a6239662b77b))
* **api:** api update ([#225](https://github.com/conductor-is/conductor-python/issues/225)) ([66767b2](https://github.com/conductor-is/conductor-python/commit/66767b2a9b803236f8c8160c193fd1a49042b357))
* **api:** api update ([#226](https://github.com/conductor-is/conductor-python/issues/226)) ([6d80050](https://github.com/conductor-is/conductor-python/commit/6d800507fe2ecb410ade2d0bec1a90d794dab43b))
* **api:** api update ([#227](https://github.com/conductor-is/conductor-python/issues/227)) ([50bb1d3](https://github.com/conductor-is/conductor-python/commit/50bb1d37416ac98b975e3cb38babe103dc036441))
* **api:** api update ([#228](https://github.com/conductor-is/conductor-python/issues/228)) ([e5a3752](https://github.com/conductor-is/conductor-python/commit/e5a3752327c2e0b33df5208005697d2f609fa147))

## 0.1.0-alpha.25 (2024-11-04)

Full Changelog: [v0.1.0-alpha.24...v0.1.0-alpha.25](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.24...v0.1.0-alpha.25)

### Features

* **api:** api update ([#211](https://github.com/conductor-is/conductor-python/issues/211)) ([e3f9f35](https://github.com/conductor-is/conductor-python/commit/e3f9f3585e57454d698e1bc5d953bd1a4f979d04))
* **api:** api update ([#213](https://github.com/conductor-is/conductor-python/issues/213)) ([91698c3](https://github.com/conductor-is/conductor-python/commit/91698c33a294cbec58a38730d7c219b5a0371db9))
* **api:** api update ([#215](https://github.com/conductor-is/conductor-python/issues/215)) ([c089b11](https://github.com/conductor-is/conductor-python/commit/c089b11fb4e65bcec6ff96cc6c5dc037cc7abe36))
* **api:** api update ([#216](https://github.com/conductor-is/conductor-python/issues/216)) ([c1816ec](https://github.com/conductor-is/conductor-python/commit/c1816ec032ab15a339d1aac16a83a5a5ad33df9c))
* **api:** api update ([#217](https://github.com/conductor-is/conductor-python/issues/217)) ([b326e2a](https://github.com/conductor-is/conductor-python/commit/b326e2adcdc619aa619303d209528303a07833f8))
* **api:** api update ([#218](https://github.com/conductor-is/conductor-python/issues/218)) ([74fb7c9](https://github.com/conductor-is/conductor-python/commit/74fb7c9e0b6af6cc8e0bb0f1f2db53fbef0448c0))
* **api:** api update ([#219](https://github.com/conductor-is/conductor-python/issues/219)) ([993490d](https://github.com/conductor-is/conductor-python/commit/993490db8e0b161238e30487a885298a5044bfe3))
* **api:** manual updates ([#214](https://github.com/conductor-is/conductor-python/issues/214)) ([3a6122b](https://github.com/conductor-is/conductor-python/commit/3a6122b66be72cb3742b4b1252dbf5a2f914cd33))

## 0.1.0-alpha.24 (2024-11-03)

Full Changelog: [v0.1.0-alpha.23...v0.1.0-alpha.24](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.23...v0.1.0-alpha.24)

### Features

* **api:** api update ([#203](https://github.com/conductor-is/conductor-python/issues/203)) ([ef9dd64](https://github.com/conductor-is/conductor-python/commit/ef9dd6416466f02010e386cff256fc866cd65e8a))
* **api:** api update ([#204](https://github.com/conductor-is/conductor-python/issues/204)) ([b654f04](https://github.com/conductor-is/conductor-python/commit/b654f0494c46407ab22224914b45c0fa39fda275))
* **api:** api update ([#205](https://github.com/conductor-is/conductor-python/issues/205)) ([4dd494b](https://github.com/conductor-is/conductor-python/commit/4dd494b4c5be748476335d8c10829aaed8dd2ee7))
* **api:** api update ([#206](https://github.com/conductor-is/conductor-python/issues/206)) ([c2c1d44](https://github.com/conductor-is/conductor-python/commit/c2c1d44d49f838c5277b01eda3bf537150e22850))
* **api:** api update ([#207](https://github.com/conductor-is/conductor-python/issues/207)) ([38dfebe](https://github.com/conductor-is/conductor-python/commit/38dfebe82f95a2932ad8b4b675e5dae62f2c8d2d))
* **api:** api update ([#208](https://github.com/conductor-is/conductor-python/issues/208)) ([e2b70ee](https://github.com/conductor-is/conductor-python/commit/e2b70ee0370d15df9d2f719990f1fdd4734b3b04))
* **api:** api update ([#209](https://github.com/conductor-is/conductor-python/issues/209)) ([154ef1c](https://github.com/conductor-is/conductor-python/commit/154ef1c8a3623ad6d4ec31e54fe238597f902ba3))
* **api:** manual updates ([#201](https://github.com/conductor-is/conductor-python/issues/201)) ([6067c05](https://github.com/conductor-is/conductor-python/commit/6067c05bfeec08288babfdf233e6284c63e23e7d))

## 0.1.0-alpha.23 (2024-11-01)

Full Changelog: [v0.1.0-alpha.22...v0.1.0-alpha.23](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.22...v0.1.0-alpha.23)

### Features

* **api:** api update ([#198](https://github.com/conductor-is/conductor-python/issues/198)) ([f4bfb1a](https://github.com/conductor-is/conductor-python/commit/f4bfb1a3b049c5f20978dcc1086acb969092fc20))
* **api:** api update ([#199](https://github.com/conductor-is/conductor-python/issues/199)) ([c55c61a](https://github.com/conductor-is/conductor-python/commit/c55c61aec269dd6ae1ac3e685133b90e0dc2599b))
* **api:** manual updates ([#195](https://github.com/conductor-is/conductor-python/issues/195)) ([aab7f65](https://github.com/conductor-is/conductor-python/commit/aab7f65cdef91a085a2ee9f7795fd08f4b6c9750))

## 0.1.0-alpha.22 (2024-10-31)

Full Changelog: [v0.1.0-alpha.21...v0.1.0-alpha.22](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.21...v0.1.0-alpha.22)

### Features

* **api:** api update ([#182](https://github.com/conductor-is/conductor-python/issues/182)) ([f5af503](https://github.com/conductor-is/conductor-python/commit/f5af50396a56d73fcdf1c05edcda8692a52ce915))
* **api:** api update ([#184](https://github.com/conductor-is/conductor-python/issues/184)) ([337f53d](https://github.com/conductor-is/conductor-python/commit/337f53db91f83ddc07cc5c079fca9ea469740628))
* **api:** api update ([#186](https://github.com/conductor-is/conductor-python/issues/186)) ([028b0cd](https://github.com/conductor-is/conductor-python/commit/028b0cd920755d690c7f4fcc1cf82937245d9dec))
* **api:** api update ([#187](https://github.com/conductor-is/conductor-python/issues/187)) ([ca329b6](https://github.com/conductor-is/conductor-python/commit/ca329b631faa671bfc56eefe4c2999eb6dface05))
* **api:** api update ([#189](https://github.com/conductor-is/conductor-python/issues/189)) ([3c8a4cb](https://github.com/conductor-is/conductor-python/commit/3c8a4cb73445a6552cf74c10f29b81853bf4f3f5))
* **api:** api update ([#192](https://github.com/conductor-is/conductor-python/issues/192)) ([92c6f6b](https://github.com/conductor-is/conductor-python/commit/92c6f6ba3ab35f82857a04d797bc49970b6b5c59))
* **api:** api update ([#194](https://github.com/conductor-is/conductor-python/issues/194)) ([fe40e44](https://github.com/conductor-is/conductor-python/commit/fe40e4428631f1647290d593c4e02c16a543ba84))
* **api:** manual updates ([#185](https://github.com/conductor-is/conductor-python/issues/185)) ([18336f6](https://github.com/conductor-is/conductor-python/commit/18336f654eef1d1c3c8fb066afb7aeb3097a7edd))
* **api:** manual updates ([#188](https://github.com/conductor-is/conductor-python/issues/188)) ([7d308c0](https://github.com/conductor-is/conductor-python/commit/7d308c06850d74816bb39b0d538c5e532f064e33))
* **api:** remove integration connections ([#190](https://github.com/conductor-is/conductor-python/issues/190)) ([77daf23](https://github.com/conductor-is/conductor-python/commit/77daf233bc5270824bd1fa479293f6a5a830e08f))


### Bug Fixes

* **internal:** remove integration connections ([4d0aee7](https://github.com/conductor-is/conductor-python/commit/4d0aee7016022c4c19b95220a7a38b701fcbdb65))


### Chores

* codegen changes ([#193](https://github.com/conductor-is/conductor-python/issues/193)) ([9e6f9bf](https://github.com/conductor-is/conductor-python/commit/9e6f9bf4f9775636c362b730ed759c578fe9f152))

## 0.1.0-alpha.21 (2024-10-30)

Full Changelog: [v0.1.0-alpha.20...v0.1.0-alpha.21](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.20...v0.1.0-alpha.21)

### Features

* **api:** api update ([#171](https://github.com/conductor-is/conductor-python/issues/171)) ([45c98a0](https://github.com/conductor-is/conductor-python/commit/45c98a0e1beb6ada649e77ac8c14fbada2258a99))
* **api:** api update ([#173](https://github.com/conductor-is/conductor-python/issues/173)) ([555ab6d](https://github.com/conductor-is/conductor-python/commit/555ab6dc99f9bb32f91d605b66936efe02839299))
* **api:** api update ([#174](https://github.com/conductor-is/conductor-python/issues/174)) ([0d53716](https://github.com/conductor-is/conductor-python/commit/0d5371650ce91a7291f97f419015219fc58d39a1))
* **api:** api update ([#175](https://github.com/conductor-is/conductor-python/issues/175)) ([df3269d](https://github.com/conductor-is/conductor-python/commit/df3269dd05135330843a79474b6afb347d0e3672))
* **api:** api update ([#176](https://github.com/conductor-is/conductor-python/issues/176)) ([4f7523d](https://github.com/conductor-is/conductor-python/commit/4f7523dffba1d2e7b3b2d0d1008d15b962e156dc))
* **api:** api update ([#178](https://github.com/conductor-is/conductor-python/issues/178)) ([55af15a](https://github.com/conductor-is/conductor-python/commit/55af15abe95640ba10fc8710d3adebf289db068e))
* **api:** api update ([#180](https://github.com/conductor-is/conductor-python/issues/180)) ([b642704](https://github.com/conductor-is/conductor-python/commit/b6427044c018fc7d6dcaa1dd030d6dd99e26a17d))
* **api:** manual updates ([#177](https://github.com/conductor-is/conductor-python/issues/177)) ([b1f9f41](https://github.com/conductor-is/conductor-python/commit/b1f9f415cdd9daf6aefd6909d028a840872d208e))
* **api:** manual updates ([#179](https://github.com/conductor-is/conductor-python/issues/179)) ([3f8b042](https://github.com/conductor-is/conductor-python/commit/3f8b042b26305874565c47649ed83f0ff1fa76fe))

## 0.1.0-alpha.20 (2024-10-29)

Full Changelog: [v0.1.0-alpha.19...v0.1.0-alpha.20](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.19...v0.1.0-alpha.20)

### Features

* **api:** api update ([#165](https://github.com/conductor-is/conductor-python/issues/165)) ([b0fc0ea](https://github.com/conductor-is/conductor-python/commit/b0fc0ea724c33073bb4f9d3e4f2dca2839437023))
* **api:** api update ([#167](https://github.com/conductor-is/conductor-python/issues/167)) ([4d2c696](https://github.com/conductor-is/conductor-python/commit/4d2c696f915580fb76e918ecf7361c8f28be47e3))
* **api:** api update ([#168](https://github.com/conductor-is/conductor-python/issues/168)) ([fb465fb](https://github.com/conductor-is/conductor-python/commit/fb465fb8daeaff3156f697351323b4654864a334))
* **api:** api update ([#169](https://github.com/conductor-is/conductor-python/issues/169)) ([58f5e6d](https://github.com/conductor-is/conductor-python/commit/58f5e6d8e21979a6b27fe9125cc45f7eb1e60533))

## 0.1.0-alpha.19 (2024-10-29)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Features

* **api:** api update ([#147](https://github.com/conductor-is/conductor-python/issues/147)) ([67767e4](https://github.com/conductor-is/conductor-python/commit/67767e4e14599cf449c3354530e54b0bc35a2d39))
* **api:** api update ([#149](https://github.com/conductor-is/conductor-python/issues/149)) ([4389fb8](https://github.com/conductor-is/conductor-python/commit/4389fb83449cbc65440eb4a774da89a515c384e7))
* **api:** api update ([#150](https://github.com/conductor-is/conductor-python/issues/150)) ([85a6f4a](https://github.com/conductor-is/conductor-python/commit/85a6f4afd94dbd7e425a216a8e436723bc040ccf))
* **api:** api update ([#151](https://github.com/conductor-is/conductor-python/issues/151)) ([d04dbb4](https://github.com/conductor-is/conductor-python/commit/d04dbb439f93f569323b0182ffdce8de6b92a1de))
* **api:** api update ([#152](https://github.com/conductor-is/conductor-python/issues/152)) ([a83abbb](https://github.com/conductor-is/conductor-python/commit/a83abbbf65b35939327dc89d577d646046a2c6d1))
* **api:** api update ([#153](https://github.com/conductor-is/conductor-python/issues/153)) ([2eb29cf](https://github.com/conductor-is/conductor-python/commit/2eb29cf7d9f318d7fb0933702606056557c63330))
* **api:** api update ([#154](https://github.com/conductor-is/conductor-python/issues/154)) ([9fa3f46](https://github.com/conductor-is/conductor-python/commit/9fa3f46e18a0f293a0cb181999afa0722998804d))
* **api:** api update ([#155](https://github.com/conductor-is/conductor-python/issues/155)) ([1fce208](https://github.com/conductor-is/conductor-python/commit/1fce2080fc7c6b70197083f45e6cec60c818d3c4))
* **api:** api update ([#156](https://github.com/conductor-is/conductor-python/issues/156)) ([2354561](https://github.com/conductor-is/conductor-python/commit/2354561e9599619ca673282d0e97312dae5e235f))
* **api:** api update ([#157](https://github.com/conductor-is/conductor-python/issues/157)) ([6e47912](https://github.com/conductor-is/conductor-python/commit/6e47912257412e44fafd17b3c046327b9a71d8d0))
* **api:** api update ([#158](https://github.com/conductor-is/conductor-python/issues/158)) ([c4698eb](https://github.com/conductor-is/conductor-python/commit/c4698eb0911657ebc0501739875a2a374f4c7c07))
* **api:** api update ([#159](https://github.com/conductor-is/conductor-python/issues/159)) ([f20a401](https://github.com/conductor-is/conductor-python/commit/f20a401a2fe03a37114e767ac9f04768929ffab3))
* **api:** api update ([#160](https://github.com/conductor-is/conductor-python/issues/160)) ([6bd488d](https://github.com/conductor-is/conductor-python/commit/6bd488d458d79794ce2f92f7c7c582447099a71c))
* **api:** api update ([#161](https://github.com/conductor-is/conductor-python/issues/161)) ([e9819fe](https://github.com/conductor-is/conductor-python/commit/e9819fe8ee99def6f8abc582f41fead58102b166))
* **api:** api update ([#162](https://github.com/conductor-is/conductor-python/issues/162)) ([6a85379](https://github.com/conductor-is/conductor-python/commit/6a85379d12f05c36204ee76c79e6f2ce4e3f8ece))
* **api:** api update ([#163](https://github.com/conductor-is/conductor-python/issues/163)) ([61806c2](https://github.com/conductor-is/conductor-python/commit/61806c2248a288004a4da4ed19c10d0797c2f681))

## 0.1.0-alpha.18 (2024-10-25)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Features

* **api:** api update ([#137](https://github.com/conductor-is/conductor-python/issues/137)) ([939b0ba](https://github.com/conductor-is/conductor-python/commit/939b0ba17571b6a2dd817769be3258087babd7a2))
* **api:** api update ([#139](https://github.com/conductor-is/conductor-python/issues/139)) ([7b0dcb6](https://github.com/conductor-is/conductor-python/commit/7b0dcb62035b4b4db51d0d8cead6587eceef64ad))
* **api:** api update ([#140](https://github.com/conductor-is/conductor-python/issues/140)) ([e5de8ce](https://github.com/conductor-is/conductor-python/commit/e5de8ce1e2bb37192d209f169376bd32d6899036))
* **api:** api update ([#141](https://github.com/conductor-is/conductor-python/issues/141)) ([0d94fa5](https://github.com/conductor-is/conductor-python/commit/0d94fa598c36d72b993ca9a9167b01a394bcab9f))
* **api:** api update ([#142](https://github.com/conductor-is/conductor-python/issues/142)) ([97b1df0](https://github.com/conductor-is/conductor-python/commit/97b1df095183b59b7efb11e6a936931e5921a545))
* **api:** api update ([#143](https://github.com/conductor-is/conductor-python/issues/143)) ([4ad6644](https://github.com/conductor-is/conductor-python/commit/4ad66446097bee2579993bb3240d136891797ae5))
* **api:** api update ([#144](https://github.com/conductor-is/conductor-python/issues/144)) ([2f8a5b1](https://github.com/conductor-is/conductor-python/commit/2f8a5b10e4d0cf1b167335867ac60ab1b971779e))
* **api:** api update ([#145](https://github.com/conductor-is/conductor-python/issues/145)) ([01cc429](https://github.com/conductor-is/conductor-python/commit/01cc429b5a66a3576de25df20e5a613135485e9c))

## 0.1.0-alpha.17 (2024-10-23)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Features

* **api:** api update ([#128](https://github.com/conductor-is/conductor-python/issues/128)) ([86990d6](https://github.com/conductor-is/conductor-python/commit/86990d6adf623cc5479685b4358429cfa3436e12))
* **api:** api update ([#130](https://github.com/conductor-is/conductor-python/issues/130)) ([1eb7883](https://github.com/conductor-is/conductor-python/commit/1eb78836746812f5bf520c0454974d225ddc0265))
* **api:** api update ([#131](https://github.com/conductor-is/conductor-python/issues/131)) ([cbaa026](https://github.com/conductor-is/conductor-python/commit/cbaa0269d458162c0de44ad97fa4850691b84573))
* **api:** api update ([#132](https://github.com/conductor-is/conductor-python/issues/132)) ([77725bc](https://github.com/conductor-is/conductor-python/commit/77725bc55910e5d4c34e70b292149e1ba0b49555))
* **api:** api update ([#133](https://github.com/conductor-is/conductor-python/issues/133)) ([e22bf3f](https://github.com/conductor-is/conductor-python/commit/e22bf3f037feacf992b949d147fc6bed80d2e02e))
* **api:** api update ([#134](https://github.com/conductor-is/conductor-python/issues/134)) ([4e539c0](https://github.com/conductor-is/conductor-python/commit/4e539c02e75f8c922408ae5baca5b1aae5399efb))
* **api:** api update ([#135](https://github.com/conductor-is/conductor-python/issues/135)) ([63dbd3e](https://github.com/conductor-is/conductor-python/commit/63dbd3ec0751bd7d4ed13ca2cd1aabcf0453233d))

## 0.1.0-alpha.16 (2024-10-22)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Features

* **api:** api update ([#122](https://github.com/conductor-is/conductor-python/issues/122)) ([5a046fe](https://github.com/conductor-is/conductor-python/commit/5a046fedea419981e6f5efc577e4f744a5fe9668))
* **api:** api update ([#124](https://github.com/conductor-is/conductor-python/issues/124)) ([f08e1d5](https://github.com/conductor-is/conductor-python/commit/f08e1d5df6e5a4ab7c00fb59c53c89bba0e6702e))
* **api:** api update ([#125](https://github.com/conductor-is/conductor-python/issues/125)) ([cefba23](https://github.com/conductor-is/conductor-python/commit/cefba23cd54badcbae9b6da3642a356164413578))
* **api:** api update ([#126](https://github.com/conductor-is/conductor-python/issues/126)) ([b5d109f](https://github.com/conductor-is/conductor-python/commit/b5d109f08852f32a15b1b954e704f848fabac6fa))

## 0.1.0-alpha.15 (2024-10-21)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** api update ([#114](https://github.com/conductor-is/conductor-python/issues/114)) ([81ceca3](https://github.com/conductor-is/conductor-python/commit/81ceca3a51deb4e0b661cdb25ac03d686cf5da17))
* **api:** api update ([#116](https://github.com/conductor-is/conductor-python/issues/116)) ([cca0685](https://github.com/conductor-is/conductor-python/commit/cca0685a54a4b1c10fde75ca906c89ffc2a0e77f))
* **api:** api update ([#117](https://github.com/conductor-is/conductor-python/issues/117)) ([3580042](https://github.com/conductor-is/conductor-python/commit/3580042d969fc1219b50cbb232cf87046802c8f7))
* **api:** api update ([#118](https://github.com/conductor-is/conductor-python/issues/118)) ([990e785](https://github.com/conductor-is/conductor-python/commit/990e78533545ddeb4761846f709200f9f192a305))
* **api:** api update ([#119](https://github.com/conductor-is/conductor-python/issues/119)) ([f8cd599](https://github.com/conductor-is/conductor-python/commit/f8cd59952c0d616987eae11e618cb16e190f3718))
* **api:** api update ([#120](https://github.com/conductor-is/conductor-python/issues/120)) ([5efe093](https://github.com/conductor-is/conductor-python/commit/5efe093f5212ac869cf40f4ec3373acd785802c9))

## 0.1.0-alpha.14 (2024-10-18)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Features

* **api:** api update ([#108](https://github.com/conductor-is/conductor-python/issues/108)) ([edc26e0](https://github.com/conductor-is/conductor-python/commit/edc26e047ed8154337e2cff94c375df609d74450))
* **api:** api update ([#110](https://github.com/conductor-is/conductor-python/issues/110)) ([3747308](https://github.com/conductor-is/conductor-python/commit/374730855a2a4e33f56d0d2b358577526b842374))
* **api:** api update ([#111](https://github.com/conductor-is/conductor-python/issues/111)) ([fd32661](https://github.com/conductor-is/conductor-python/commit/fd32661d6314e409afc919118566efcf765e9bbf))
* **api:** api update ([#112](https://github.com/conductor-is/conductor-python/issues/112)) ([f119dad](https://github.com/conductor-is/conductor-python/commit/f119dadd355793e4492d8b4940862619e3676a70))

## 0.1.0-alpha.13 (2024-10-18)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Features

* **api:** api update ([#101](https://github.com/conductor-is/conductor-python/issues/101)) ([af68f23](https://github.com/conductor-is/conductor-python/commit/af68f238e90d7e404bfb33464ba842b627f91e69))
* **api:** api update ([#103](https://github.com/conductor-is/conductor-python/issues/103)) ([47a729a](https://github.com/conductor-is/conductor-python/commit/47a729a7c462fb54f67a339e769c671cfcb27198))
* **api:** api update ([#104](https://github.com/conductor-is/conductor-python/issues/104)) ([dcaa703](https://github.com/conductor-is/conductor-python/commit/dcaa70341afb31882d48f5f73e783af49427990d))
* **api:** api update ([#105](https://github.com/conductor-is/conductor-python/issues/105)) ([1f77dd2](https://github.com/conductor-is/conductor-python/commit/1f77dd2649cc380b56e7985f96ab7c11bcfb5a26))
* **api:** api update ([#106](https://github.com/conductor-is/conductor-python/issues/106)) ([96c29f8](https://github.com/conductor-is/conductor-python/commit/96c29f8db72b2f290ac5525268deb20147b08b10))

## 0.1.0-alpha.12 (2024-10-17)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** api update ([#96](https://github.com/conductor-is/conductor-python/issues/96)) ([8aaa8b4](https://github.com/conductor-is/conductor-python/commit/8aaa8b46a7087e227bf0f4ac9872d9b296d02e94))
* **api:** api update ([#98](https://github.com/conductor-is/conductor-python/issues/98)) ([caf272a](https://github.com/conductor-is/conductor-python/commit/caf272a870faf890cd3eb754e63e3a23502966b5))
* **api:** api update ([#99](https://github.com/conductor-is/conductor-python/issues/99)) ([69373ee](https://github.com/conductor-is/conductor-python/commit/69373ee118fe9ba8430503a90466b6264877765c))

## 0.1.0-alpha.11 (2024-10-17)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Features

* **api:** api update ([#92](https://github.com/conductor-is/conductor-python/issues/92)) ([b9c82e8](https://github.com/conductor-is/conductor-python/commit/b9c82e81841692cf7eaaf999ce6990c3478940cd))
* **api:** api update ([#94](https://github.com/conductor-is/conductor-python/issues/94)) ([b19f258](https://github.com/conductor-is/conductor-python/commit/b19f25850980fbcacbea7820ad9680335ccad20b))

## 0.1.0-alpha.10 (2024-10-16)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **api:** api update ([#88](https://github.com/conductor-is/conductor-python/issues/88)) ([47528b8](https://github.com/conductor-is/conductor-python/commit/47528b8f9adc1bbcc9fa8546e706773bde3e53da))
* **api:** api update ([#90](https://github.com/conductor-is/conductor-python/issues/90)) ([041768f](https://github.com/conductor-is/conductor-python/commit/041768ffbfa1c651672714522c3f1fc9b3b41acd))

## 0.1.0-alpha.9 (2024-10-15)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** api update ([#85](https://github.com/conductor-is/conductor-python/issues/85)) ([25aadd4](https://github.com/conductor-is/conductor-python/commit/25aadd46efa964e8e67af36944117c948f4537da))

## 0.1.0-alpha.8 (2024-10-15)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** api update ([#74](https://github.com/conductor-is/conductor-python/issues/74)) ([d78d12d](https://github.com/conductor-is/conductor-python/commit/d78d12dd6e67e81ac9aeda72d19872e75d97f4ee))
* **api:** api update ([#76](https://github.com/conductor-is/conductor-python/issues/76)) ([d9707ac](https://github.com/conductor-is/conductor-python/commit/d9707ac5b91294665635024d522607cf5c292473))
* **api:** api update ([#77](https://github.com/conductor-is/conductor-python/issues/77)) ([ce621f4](https://github.com/conductor-is/conductor-python/commit/ce621f49a6359146915c4b6708b8ebee93dde0ac))
* **api:** api update ([#78](https://github.com/conductor-is/conductor-python/issues/78)) ([9bbbefc](https://github.com/conductor-is/conductor-python/commit/9bbbefcdef97e8cae0da28ca4e22d08d847e63b4))
* **api:** api update ([#79](https://github.com/conductor-is/conductor-python/issues/79)) ([2531f9a](https://github.com/conductor-is/conductor-python/commit/2531f9a7feb82f64061f1b936222905113af7568))
* **api:** api update ([#80](https://github.com/conductor-is/conductor-python/issues/80)) ([4d9bcd4](https://github.com/conductor-is/conductor-python/commit/4d9bcd4919853a43bc7eb79637597d885f918819))
* **api:** api update ([#81](https://github.com/conductor-is/conductor-python/issues/81)) ([b68a9f0](https://github.com/conductor-is/conductor-python/commit/b68a9f0dacdb62f66eb272a1de09e0073afafa34))
* **api:** api update ([#82](https://github.com/conductor-is/conductor-python/issues/82)) ([3088198](https://github.com/conductor-is/conductor-python/commit/308819821a26c5a1af87d7a096098b4adc56a72a))
* **api:** api update ([#83](https://github.com/conductor-is/conductor-python/issues/83)) ([5e412c9](https://github.com/conductor-is/conductor-python/commit/5e412c9ba388aca61a2cfa8b2709d75779664d94))

## 0.1.0-alpha.7 (2024-10-13)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** api update ([#64](https://github.com/conductor-is/conductor-python/issues/64)) ([be0d706](https://github.com/conductor-is/conductor-python/commit/be0d7065ee51175487b8005e62d9d06f7a5ecbfc))
* **api:** api update ([#66](https://github.com/conductor-is/conductor-python/issues/66)) ([13c840a](https://github.com/conductor-is/conductor-python/commit/13c840a629c0d7a50456ecf47b274153f4faa0ab))
* **api:** api update ([#67](https://github.com/conductor-is/conductor-python/issues/67)) ([54e5574](https://github.com/conductor-is/conductor-python/commit/54e5574c0c878db84febda4bf57093cf61fccb7f))
* **api:** api update ([#68](https://github.com/conductor-is/conductor-python/issues/68)) ([d6b7732](https://github.com/conductor-is/conductor-python/commit/d6b77326ffe72049bf4ca9e79d137bf7d5236fee))
* **api:** api update ([#69](https://github.com/conductor-is/conductor-python/issues/69)) ([6f92519](https://github.com/conductor-is/conductor-python/commit/6f92519a728c9630178ed641881738afce8e91ae))
* **api:** api update ([#70](https://github.com/conductor-is/conductor-python/issues/70)) ([157b28a](https://github.com/conductor-is/conductor-python/commit/157b28a93fb9e3c540f2fc68adab6b7bba34b975))

## 0.1.0-alpha.6 (2024-10-11)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** api update ([#54](https://github.com/conductor-is/conductor-python/issues/54)) ([eb97202](https://github.com/conductor-is/conductor-python/commit/eb97202f7585b7285531c59684d27bede40ef65a))
* **api:** api update ([#55](https://github.com/conductor-is/conductor-python/issues/55)) ([a11a233](https://github.com/conductor-is/conductor-python/commit/a11a23325b622b55bba42da190dca9fb1abd3c01))
* **api:** api update ([#56](https://github.com/conductor-is/conductor-python/issues/56)) ([d75fe5c](https://github.com/conductor-is/conductor-python/commit/d75fe5c0182c74e31e8caf66ecf4272a0d0855a8))
* **api:** api update ([#57](https://github.com/conductor-is/conductor-python/issues/57)) ([028221b](https://github.com/conductor-is/conductor-python/commit/028221bd3fafe30ac1748211f25ad041143d43b7))
* **api:** api update ([#58](https://github.com/conductor-is/conductor-python/issues/58)) ([3da87a3](https://github.com/conductor-is/conductor-python/commit/3da87a3896b069ba2b9caa91aed12ca7ca0becec))
* **api:** api update ([#59](https://github.com/conductor-is/conductor-python/issues/59)) ([72e66d8](https://github.com/conductor-is/conductor-python/commit/72e66d86398016171d5db70faf4d3c00eb19a029))
* **api:** api update ([#60](https://github.com/conductor-is/conductor-python/issues/60)) ([9e1cfc5](https://github.com/conductor-is/conductor-python/commit/9e1cfc5883d1f5bb39ffa296589e3ffc8f60ca91))
* **api:** api update ([#61](https://github.com/conductor-is/conductor-python/issues/61)) ([b8500c9](https://github.com/conductor-is/conductor-python/commit/b8500c9a5f47d7d24506bf5298e6ef5888e2501a))
* **api:** manual updates ([#48](https://github.com/conductor-is/conductor-python/issues/48)) ([937a294](https://github.com/conductor-is/conductor-python/commit/937a29406616ac3b157a40cf57afb5b2fa2d4eb1))
* **api:** OpenAPI spec update via Stainless API ([#44](https://github.com/conductor-is/conductor-python/issues/44)) ([833e15c](https://github.com/conductor-is/conductor-python/commit/833e15cc216753635a4b9b675a55933207605952))
* **api:** OpenAPI spec update via Stainless API ([#49](https://github.com/conductor-is/conductor-python/issues/49)) ([1acf56d](https://github.com/conductor-is/conductor-python/commit/1acf56d3d3d6227597c42d4aca3880149c0801a6))
* **api:** OpenAPI spec update via Stainless API ([#50](https://github.com/conductor-is/conductor-python/issues/50)) ([95b0cf7](https://github.com/conductor-is/conductor-python/commit/95b0cf7a5c82de9fecb8f602b0fe14a988c817a2))
* **api:** OpenAPI spec update via Stainless API ([#51](https://github.com/conductor-is/conductor-python/issues/51)) ([45d59e1](https://github.com/conductor-is/conductor-python/commit/45d59e15a9e26e6f3beacf901e539825944d306f))
* **api:** OpenAPI spec update via Stainless API ([#52](https://github.com/conductor-is/conductor-python/issues/52)) ([d8b2520](https://github.com/conductor-is/conductor-python/commit/d8b2520898dcc42d284545cacb9fef304aa8b47f))
* **api:** OpenAPI spec update via Stainless API ([#53](https://github.com/conductor-is/conductor-python/issues/53)) ([8d18a81](https://github.com/conductor-is/conductor-python/commit/8d18a81da2d72c8320cf250aa6d90d9868757a5e))


### Bug Fixes

* **client:** avoid OverflowError with very large retry counts ([#46](https://github.com/conductor-is/conductor-python/issues/46)) ([169b02c](https://github.com/conductor-is/conductor-python/commit/169b02cab2670283bcb4fdca71f97273e25dde82))


### Chores

* add repr to PageInfo class ([#47](https://github.com/conductor-is/conductor-python/issues/47)) ([de0c019](https://github.com/conductor-is/conductor-python/commit/de0c0191d7c082bef2050a5225bd325b46233068))

## 0.1.0-alpha.5 (2024-10-06)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** update via SDK Studio ([#38](https://github.com/conductor-is/conductor-python/issues/38)) ([2ea197b](https://github.com/conductor-is/conductor-python/commit/2ea197ba93ee128b07697900af32d1eadd959fc9))


### Chores

* **internal:** add support for parsing bool response content ([#42](https://github.com/conductor-is/conductor-python/issues/42)) ([b59e831](https://github.com/conductor-is/conductor-python/commit/b59e831d1a32f4f23f392ec634f2154fba1c06b5))
* **internal:** codegen related update ([#40](https://github.com/conductor-is/conductor-python/issues/40)) ([f759a7a](https://github.com/conductor-is/conductor-python/commit/f759a7a89512509169e0f8ded4bd7d2ce3e2d147))
* **internal:** codegen related update ([#41](https://github.com/conductor-is/conductor-python/issues/41)) ([3e863ee](https://github.com/conductor-is/conductor-python/commit/3e863ee5cf5418a95ab884b17d5bc1cb511b6aa0))

## 0.1.0-alpha.4 (2024-09-30)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** update via SDK Studio ([#27](https://github.com/conductor-is/conductor-python/issues/27)) ([889eca4](https://github.com/conductor-is/conductor-python/commit/889eca4a6fc284f5ef954a972e88cd8640b82b22))
* **api:** update via SDK Studio ([#29](https://github.com/conductor-is/conductor-python/issues/29)) ([1b59254](https://github.com/conductor-is/conductor-python/commit/1b592549e266594ca0abb7bcdb104be7f1cd7ebb))
* **api:** update via SDK Studio ([#30](https://github.com/conductor-is/conductor-python/issues/30)) ([fa7c51a](https://github.com/conductor-is/conductor-python/commit/fa7c51ad61d34a2fe9e26925a1d7cf26990d41df))
* **api:** update via SDK Studio ([#33](https://github.com/conductor-is/conductor-python/issues/33)) ([7f0f5ee](https://github.com/conductor-is/conductor-python/commit/7f0f5ee693cb0c0a90b652e8ed9a8e1228f147df))
* **client:** send retry count header ([#32](https://github.com/conductor-is/conductor-python/issues/32)) ([10faf81](https://github.com/conductor-is/conductor-python/commit/10faf813124c37b08113d7de41f3920bd1886a0c))


### Bug Fixes

* **client:** handle domains with underscores ([#31](https://github.com/conductor-is/conductor-python/issues/31)) ([8e750e1](https://github.com/conductor-is/conductor-python/commit/8e750e1a6799fea10221d09e7fc38fb2bfe9163f))


### Chores

* **internal:** codegen related update ([#35](https://github.com/conductor-is/conductor-python/issues/35)) ([52c3970](https://github.com/conductor-is/conductor-python/commit/52c3970e956893a39e7bba9399538b7646901aca))
* **internal:** codegen related update ([#36](https://github.com/conductor-is/conductor-python/issues/36)) ([31d4ef4](https://github.com/conductor-is/conductor-python/commit/31d4ef47f4da3f0f508d8f50a1b164ea1ce194d2))
* **internal:** update pydantic v1 compat helpers ([#34](https://github.com/conductor-is/conductor-python/issues/34)) ([68fffdb](https://github.com/conductor-is/conductor-python/commit/68fffdb97d5f765d59df9588fcb1577fd569f608))

## 0.1.0-alpha.3 (2024-09-18)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Features

* **api:** update via SDK Studio ([#16](https://github.com/conductor-is/conductor-python/issues/16)) ([db50bae](https://github.com/conductor-is/conductor-python/commit/db50bae0dcd000a0a4697a8042327ad9ad7f05b4))
* **api:** update via SDK Studio ([#18](https://github.com/conductor-is/conductor-python/issues/18)) ([b18af59](https://github.com/conductor-is/conductor-python/commit/b18af595f682ccf653f82d3cba776b57171547e1))
* **api:** update via SDK Studio ([#19](https://github.com/conductor-is/conductor-python/issues/19)) ([83aeedd](https://github.com/conductor-is/conductor-python/commit/83aeedd330ff2a890322e32b64a98862d6df0c9b))
* **api:** update via SDK Studio ([#22](https://github.com/conductor-is/conductor-python/issues/22)) ([d820537](https://github.com/conductor-is/conductor-python/commit/d82053740ad57792048b477ee3b92dc78e1e7fc3))
* **api:** update via SDK Studio ([#23](https://github.com/conductor-is/conductor-python/issues/23)) ([26f5d61](https://github.com/conductor-is/conductor-python/commit/26f5d61f657cddc5bb1d9ae386d7477872e73f32))
* **api:** update via SDK Studio ([#24](https://github.com/conductor-is/conductor-python/issues/24)) ([820c8c3](https://github.com/conductor-is/conductor-python/commit/820c8c384286e3a7c79a40832a0426f7eb7302c4))
* **api:** update via SDK Studio ([#25](https://github.com/conductor-is/conductor-python/issues/25)) ([d1fc04b](https://github.com/conductor-is/conductor-python/commit/d1fc04b036c23c03316cf91cdc4d897959458ca9))


### Chores

* add docstrings to raw response properties ([#13](https://github.com/conductor-is/conductor-python/issues/13)) ([6300c96](https://github.com/conductor-is/conductor-python/commit/6300c9613a7a056cc2ad21a401730a148a59da4a))
* **internal:** bump pyright / mypy version ([#21](https://github.com/conductor-is/conductor-python/issues/21)) ([a6e8897](https://github.com/conductor-is/conductor-python/commit/a6e8897535da4f3a396badb4c3fe34455c32beb6))
* **internal:** bump ruff ([#20](https://github.com/conductor-is/conductor-python/issues/20)) ([9e245df](https://github.com/conductor-is/conductor-python/commit/9e245df647a688ede26f8d79e3c42612cd5a8766))


### Documentation

* **readme:** add section on determining installed version ([#14](https://github.com/conductor-is/conductor-python/issues/14)) ([b7c9f8b](https://github.com/conductor-is/conductor-python/commit/b7c9f8bb1f96d2c256a229fd3321f4ce7def744e))
* update CONTRIBUTING.md ([#17](https://github.com/conductor-is/conductor-python/issues/17)) ([96cb918](https://github.com/conductor-is/conductor-python/commit/96cb918d7393283736cd6e29b8b0b034cd81aece))

## 0.1.0-alpha.2 (2024-09-08)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/conductor-is/conductor-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** update via SDK Studio ([#11](https://github.com/conductor-is/conductor-python/issues/11)) ([fb69258](https://github.com/conductor-is/conductor-python/commit/fb69258a1df4e3cee8fa6ebe056b0336724b2c1f))
* **api:** update via SDK Studio ([#7](https://github.com/conductor-is/conductor-python/issues/7)) ([6708001](https://github.com/conductor-is/conductor-python/commit/670800117c6222c8ee30f85f2c90f7e114b73302))


### Chores

* pyproject.toml formatting changes ([#9](https://github.com/conductor-is/conductor-python/issues/9)) ([ceac058](https://github.com/conductor-is/conductor-python/commit/ceac0582eb3ebb352bbf9ce26e930d40eb9b39f6))

## 0.1.0-alpha.1 (2024-09-02)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/conductor-is/conductor-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** update via SDK Studio ([b6472f6](https://github.com/conductor-is/conductor-python/commit/b6472f626e01f0db7d43f7877bf2f5e2ecf5fddb))
* **api:** update via SDK Studio ([#4](https://github.com/conductor-is/conductor-python/issues/4)) ([c211314](https://github.com/conductor-is/conductor-python/commit/c2113146925f252addb52f99a25a0ac0e873597a))
* **api:** update via SDK Studio ([#5](https://github.com/conductor-is/conductor-python/issues/5)) ([253d78c](https://github.com/conductor-is/conductor-python/commit/253d78c50259ec7e1cde2d66a6cfcc137252bc0b))


### Chores

* go live ([#1](https://github.com/conductor-is/conductor-python/issues/1)) ([4be56ce](https://github.com/conductor-is/conductor-python/commit/4be56ce217400f0013c503ccdf82f96b0abe35c4))
* update SDK settings ([#3](https://github.com/conductor-is/conductor-python/issues/3)) ([f042384](https://github.com/conductor-is/conductor-python/commit/f04238468a1f22471e26f5bcd8b3e97a59ca4af9))
