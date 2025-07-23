# Changelog

## 0.1.0-alpha.19 (2025-07-23)

Full Changelog: [v0.1.0-alpha.18...v0.1.0-alpha.19](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.18...v0.1.0-alpha.19)

### Bug Fixes

* **parsing:** parse extra field types ([556dd44](https://github.com/DatagridAI/datagrid-python/commit/556dd44012acef8e2e3aec3e2f389d5561047d29))

## 0.1.0-alpha.18 (2025-07-22)

Full Changelog: [v0.1.0-alpha.17...v0.1.0-alpha.18](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.17...v0.1.0-alpha.18)

### Features

* clean up environment call outs ([7cc9b31](https://github.com/DatagridAI/datagrid-python/commit/7cc9b315a597741958907b334dc0022652e42730))


### Bug Fixes

* **parsing:** ignore empty metadata ([f5884fb](https://github.com/DatagridAI/datagrid-python/commit/f5884fbd1b60bb73ec9908893c2332751dcb4828))

## 0.1.0-alpha.17 (2025-07-12)

Full Changelog: [v0.1.0-alpha.16...v0.1.0-alpha.17](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.16...v0.1.0-alpha.17)

### Bug Fixes

* **client:** don't send Content-Type header on GET requests ([4732ccc](https://github.com/DatagridAI/datagrid-python/commit/4732cccf189fa83ec1c1838e32288b341fb508e5))


### Chores

* **readme:** fix version rendering on pypi ([83e8f48](https://github.com/DatagridAI/datagrid-python/commit/83e8f48587fad3c4fb81522632502046bc688273))

## 0.1.0-alpha.16 (2025-07-10)

Full Changelog: [v0.1.0-alpha.15...v0.1.0-alpha.16](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.15...v0.1.0-alpha.16)

### Bug Fixes

* **parsing:** correctly handle nested discriminated unions ([8db4008](https://github.com/DatagridAI/datagrid-python/commit/8db400826d2c272fa9ac3aef1c42e7bb07884882))


### Chores

* **internal:** bump pinned h11 dep ([f658efc](https://github.com/DatagridAI/datagrid-python/commit/f658efc24fb9a2df8b4e2a4acf0fd768c72020d4))
* **package:** mark python 3.13 as supported ([bf4ec47](https://github.com/DatagridAI/datagrid-python/commit/bf4ec471f9ec2bfeb64f632eda4693a4fc8de54c))

## 0.1.0-alpha.15 (2025-07-04)

Full Changelog: [v0.1.0-alpha.14...v0.1.0-alpha.15](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.14...v0.1.0-alpha.15)

### Features

* **api:** api update ([811c9b8](https://github.com/DatagridAI/datagrid-python/commit/811c9b81e94b6bf5704a78ef4a832cc09b5e0751))


### Chores

* **ci:** change upload type ([4e2f02c](https://github.com/DatagridAI/datagrid-python/commit/4e2f02cae19e106f00e5df1d232a12f023ea3266))

## 0.1.0-alpha.14 (2025-06-30)

Full Changelog: [v0.1.0-alpha.13...v0.1.0-alpha.14](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.13...v0.1.0-alpha.14)

### Bug Fixes

* **ci:** correct conditional ([6f8ff47](https://github.com/DatagridAI/datagrid-python/commit/6f8ff471850a13b1f708202e62447ac229516cca))


### Chores

* **ci:** only run for pushes and fork pull requests ([7f3dac3](https://github.com/DatagridAI/datagrid-python/commit/7f3dac3e1210be75377890c3f7ede8094fbc497b))

## 0.1.0-alpha.13 (2025-06-27)

Full Changelog: [v0.1.0-alpha.12...v0.1.0-alpha.13](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.12...v0.1.0-alpha.13)

### Bug Fixes

* **ci:** release-doctor — report correct token name ([e3db8d6](https://github.com/DatagridAI/datagrid-python/commit/e3db8d60a1de6a9bc0078b072a241268538e2f61))


### Chores

* **tests:** skip some failing tests on the latest python versions ([ab78ea3](https://github.com/DatagridAI/datagrid-python/commit/ab78ea360c718461a625214638325d145e58ee15))

## 0.1.0-alpha.12 (2025-06-23)

Full Changelog: [v0.1.0-alpha.11...v0.1.0-alpha.12](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.11...v0.1.0-alpha.12)

### Features

* **api:** api update ([97b7538](https://github.com/DatagridAI/datagrid-python/commit/97b753863e3a06eb7d5a6423ac389b5a1d75ad52))
* **client:** add support for aiohttp ([b304bb4](https://github.com/DatagridAI/datagrid-python/commit/b304bb47e44d39bd29d8d5d322cd552ae2b2f8b9))


### Documentation

* **client:** fix httpx.Timeout documentation reference ([d51d6cd](https://github.com/DatagridAI/datagrid-python/commit/d51d6cd68237bc2f88670d509b986684b6a3d6ce))

## 0.1.0-alpha.11 (2025-06-18)

Full Changelog: [v0.1.0-alpha.10...v0.1.0-alpha.11](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.10...v0.1.0-alpha.11)

### Bug Fixes

* **tests:** fix: tests which call HTTP endpoints directly with the example parameters ([4dd9a53](https://github.com/DatagridAI/datagrid-python/commit/4dd9a53b654967f9e5d9ee6f84cd80dcf4b9734a))


### Chores

* **ci:** enable for pull requests ([a07a3c0](https://github.com/DatagridAI/datagrid-python/commit/a07a3c0f1ad7869f4078687e9f19b8d597458fdf))
* **internal:** update conftest.py ([962a1ac](https://github.com/DatagridAI/datagrid-python/commit/962a1acdaba134e06cc4370fed0fd85aa22b4313))
* **readme:** update badges ([e63d5b8](https://github.com/DatagridAI/datagrid-python/commit/e63d5b8b4538f0a1fcd71b31862a6f60f47de359))
* **tests:** add tests for httpx client instantiation & proxies ([1e7b9e8](https://github.com/DatagridAI/datagrid-python/commit/1e7b9e81bcbe864b60541a1d5e42df41e7d8d370))

## 0.1.0-alpha.10 (2025-06-13)

Full Changelog: [v0.1.0-alpha.9...v0.1.0-alpha.10](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.9...v0.1.0-alpha.10)

### Features

* **client:** add follow_redirects request option ([5c794ae](https://github.com/DatagridAI/datagrid-python/commit/5c794ae0ed92b3669a5fcb0d5884cea3f96cbb1b))


### Bug Fixes

* **client:** correctly parse binary response | stream ([03be065](https://github.com/DatagridAI/datagrid-python/commit/03be065c4e07a8cc7def153f131b80d872aef7e8))


### Chores

* **docs:** remove reference to rye shell ([ef6eee4](https://github.com/DatagridAI/datagrid-python/commit/ef6eee4fc57446563961f69590d717d207b82760))
* **docs:** remove unnecessary param examples ([f09ed5e](https://github.com/DatagridAI/datagrid-python/commit/f09ed5ec8c93c8e74ef11ec561eefc706ea60954))
* **tests:** run tests in parallel ([a4d5067](https://github.com/DatagridAI/datagrid-python/commit/a4d506709f15ac43062baaf759ef6333a5b16648))

## 0.1.0-alpha.9 (2025-06-01)

Full Changelog: [v0.1.0-alpha.8...v0.1.0-alpha.9](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.8...v0.1.0-alpha.9)

### Features

* **api:** api update ([0ad7592](https://github.com/DatagridAI/datagrid-python/commit/0ad7592206a7e680e8aafdc1b6c9bc881a7c4c5e))
* **api:** api update ([f034485](https://github.com/DatagridAI/datagrid-python/commit/f034485d95f21eec4d13f4fd7f220264e1f37318))

## 0.1.0-alpha.8 (2025-05-26)

Full Changelog: [v0.1.0-alpha.7...v0.1.0-alpha.8](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.7...v0.1.0-alpha.8)

### Features

* **api:** api update ([aea656c](https://github.com/DatagridAI/datagrid-python/commit/aea656c2ab600a852c00a334f613e98206d554e6))
* **api:** api update ([1389cc2](https://github.com/DatagridAI/datagrid-python/commit/1389cc212729fa13bb70bbe3b8090235d8a6f789))
* **api:** api update ([2fba8c9](https://github.com/DatagridAI/datagrid-python/commit/2fba8c901ccd767d60970e9cabb10d5d427354b9))
* **api:** api update ([9e42c13](https://github.com/DatagridAI/datagrid-python/commit/9e42c13e25ba478b40dcceeca93c668a4589730d))
* **api:** api update ([2cfc00c](https://github.com/DatagridAI/datagrid-python/commit/2cfc00cce15bb7ea89af7290c020799cef1738ed))
* **api:** api update ([3f7a4b6](https://github.com/DatagridAI/datagrid-python/commit/3f7a4b6f54df771231c0dbe607b3245f63c5f375))
* **api:** api update ([2eced62](https://github.com/DatagridAI/datagrid-python/commit/2eced625be77bfaa14acd5ebd3abe16060a61dc1))


### Bug Fixes

* **package:** support direct resource imports ([6aa3ba4](https://github.com/DatagridAI/datagrid-python/commit/6aa3ba4ab0790575ad5711c6e929939a58a19a1b))
* **package:** support direct resource imports ([79ab574](https://github.com/DatagridAI/datagrid-python/commit/79ab574c90bcd5c3b3d04980e1ce5afe48a5393d))
* **perf:** optimize some hot paths ([a69daa1](https://github.com/DatagridAI/datagrid-python/commit/a69daa1c5169ff72bc537df7b18c4c50152e7286))
* **perf:** skip traversing types for NotGiven values ([414feb0](https://github.com/DatagridAI/datagrid-python/commit/414feb0c31bc502bc3546582053069f933c3f85f))
* **pydantic v1:** more robust ModelField.annotation check ([146f01d](https://github.com/DatagridAI/datagrid-python/commit/146f01d0e7169be367ca05028168460ccf612069))


### Chores

* broadly detect json family of content-type headers ([8a68411](https://github.com/DatagridAI/datagrid-python/commit/8a684111c8d66787c5daee7893e1ba81ab545be3))
* **ci:** add timeout thresholds for CI jobs ([1457fc3](https://github.com/DatagridAI/datagrid-python/commit/1457fc387d89dc9eb9e7cf66d0c636aae74bf079))
* **ci:** fix installation instructions ([fa43889](https://github.com/DatagridAI/datagrid-python/commit/fa4388974b31ae164cc7f8a79f70547e3cf9baee))
* **ci:** fix installation instructions ([519082b](https://github.com/DatagridAI/datagrid-python/commit/519082b94778805c818e44644356d7b3994e8518))
* **ci:** only use depot for staging repos ([7ed9b36](https://github.com/DatagridAI/datagrid-python/commit/7ed9b36be8b24b7cbb2acf98f974d49335ce16b9))
* **ci:** upload sdks to package manager ([237bec1](https://github.com/DatagridAI/datagrid-python/commit/237bec1db34fa84cc91e9fbe4d262850ae4f4ec8))
* **ci:** upload sdks to package manager ([c7f7994](https://github.com/DatagridAI/datagrid-python/commit/c7f7994d05bb2c09f9e23860d67d47bf5582fde8))
* **client:** minor internal fixes ([bb6292d](https://github.com/DatagridAI/datagrid-python/commit/bb6292d31ff45618bd588933e236f01fbf729fac))
* **docs:** grammar improvements ([6dda73b](https://github.com/DatagridAI/datagrid-python/commit/6dda73bca8237e5bbe40501ce4ea4dd2c6a6a18f))
* **docs:** grammar improvements ([e3e01f1](https://github.com/DatagridAI/datagrid-python/commit/e3e01f1a3df3a966ec9ddf7b003055b88545bdb2))
* **internal:** avoid errors for isinstance checks on proxies ([e3c5849](https://github.com/DatagridAI/datagrid-python/commit/e3c5849536afd935133809262975c357acffb538))
* **internal:** avoid errors for isinstance checks on proxies ([8466e9d](https://github.com/DatagridAI/datagrid-python/commit/8466e9d00af69df60fe3195560545620b917d0ad))
* **internal:** base client updates ([74039a9](https://github.com/DatagridAI/datagrid-python/commit/74039a90bac677cdb4ecd9ff41167c9055660cf8))
* **internal:** bump pyright version ([77d0e04](https://github.com/DatagridAI/datagrid-python/commit/77d0e0418254c204eab6fb854d488ccf3fb02d7b))
* **internal:** codegen related update ([fbc4788](https://github.com/DatagridAI/datagrid-python/commit/fbc4788e7c796fa8fb6d44cd29c8f4a68b66e2da))
* **internal:** codegen related update ([8119d34](https://github.com/DatagridAI/datagrid-python/commit/8119d347b0f334c56d94c3787a9c05b9b77f28dd))
* **internal:** codegen related update ([e4a139c](https://github.com/DatagridAI/datagrid-python/commit/e4a139cfe2d534b6006022e48e0c845012097640))
* **internal:** expand CI branch coverage ([7d209af](https://github.com/DatagridAI/datagrid-python/commit/7d209af6c136f63d93bdcd96a7fd29a2240b1160))
* **internal:** fix list file params ([c4351ad](https://github.com/DatagridAI/datagrid-python/commit/c4351adc26a005c36216aa69474f4f2383d76207))
* **internal:** import reformatting ([752a0a6](https://github.com/DatagridAI/datagrid-python/commit/752a0a66d0f870d9b72a02ab132230ef8188ec12))
* **internal:** reduce CI branch coverage ([57d7ee4](https://github.com/DatagridAI/datagrid-python/commit/57d7ee431da0fb6f254326aec135091afae89056))
* **internal:** refactor retries to not use recursion ([bfc18e5](https://github.com/DatagridAI/datagrid-python/commit/bfc18e59a26e61857c5d6f3ea46aec4c4f352550))
* **internal:** remove trailing character ([03603f3](https://github.com/DatagridAI/datagrid-python/commit/03603f38fe84988f4c65b0719ccd5592a85bc59b))
* **internal:** slight transform perf improvement ([a52f0ef](https://github.com/DatagridAI/datagrid-python/commit/a52f0ef31f266fe06c159f6016cb6776a02450bd))
* **internal:** update file param examples ([19ce6f7](https://github.com/DatagridAI/datagrid-python/commit/19ce6f71a86377b5f2bc9f9715ea99ca82fb705e))
* **internal:** update models test ([971e32a](https://github.com/DatagridAI/datagrid-python/commit/971e32a83a6c989f09c73b9762af93a43241c9f1))
* **internal:** update pyright settings ([eb4dae9](https://github.com/DatagridAI/datagrid-python/commit/eb4dae9b15bc335d0c0fde519500daa7e5159e11))
* **internal:** version bump ([#24](https://github.com/DatagridAI/datagrid-python/issues/24)) ([f850000](https://github.com/DatagridAI/datagrid-python/commit/f850000c03228166a29845fc18b6b4e2b2c6c9d3))
* update SDK settings ([b4bfae6](https://github.com/DatagridAI/datagrid-python/commit/b4bfae697b07d2ff8fcab69a5c843ec07903cdab))
* update SDK settings ([5af1a58](https://github.com/DatagridAI/datagrid-python/commit/5af1a584341a893357a148e3cccf1d462542e53b))
* update SDK settings ([37733b7](https://github.com/DatagridAI/datagrid-python/commit/37733b7c7d83ab1a717406fafeb2af742d248a0a))
* update SDK settings ([db8780d](https://github.com/DatagridAI/datagrid-python/commit/db8780d77cf39f92deec8a00e83c4c5215c2d400))
* update SDK settings ([6851c91](https://github.com/DatagridAI/datagrid-python/commit/6851c91ff6cca9b42d8d9b7dc6039cd626cedfb5))

## 0.1.0-alpha.7 (2025-04-03)

Full Changelog: [v0.1.0-alpha.6...v0.1.0-alpha.7](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.6...v0.1.0-alpha.7)

### Features

* **api:** api update ([6024f2c](https://github.com/DatagridAI/datagrid-python/commit/6024f2c26df9aefde5cc396f0ac76daee22e555c))
* **api:** api update ([9f8986d](https://github.com/DatagridAI/datagrid-python/commit/9f8986d7f2537250fa02e53ecbdcada4750db896))
* **api:** api update ([ec3c727](https://github.com/DatagridAI/datagrid-python/commit/ec3c727b772116faea0d64d9f72eee4727af49a8))
* **api:** api update ([366491b](https://github.com/DatagridAI/datagrid-python/commit/366491b88ccdb9d698faa7d19f530561992e775c))
* **api:** api update ([fdd0edf](https://github.com/DatagridAI/datagrid-python/commit/fdd0edf3ec67058a347d4b47d1f6c657c50b86e1))


### Bug Fixes

* **ci:** ensure pip is always available ([7333b0f](https://github.com/DatagridAI/datagrid-python/commit/7333b0fb136954b1f490fc51c42b3598d3bbc284))
* **ci:** remove publishing patch ([23fbdd8](https://github.com/DatagridAI/datagrid-python/commit/23fbdd82d9fbe918c8ef28d9a437eb2a21061899))
* **types:** handle more discriminated union shapes ([60b6945](https://github.com/DatagridAI/datagrid-python/commit/60b694538e89756badf3bc1eb5e45c2a86f312bb))


### Chores

* fix typos ([6d417a0](https://github.com/DatagridAI/datagrid-python/commit/6d417a0466ca5ce33f653c1114af4e18e19669e4))
* go live ([9b4fbf1](https://github.com/DatagridAI/datagrid-python/commit/9b4fbf195e38ceaab87ed93ffd086f9cfd8750ef))
* go live ([938c836](https://github.com/DatagridAI/datagrid-python/commit/938c836827490764e550b2fd2c42874125f0e514))
* go live ([#17](https://github.com/DatagridAI/datagrid-python/issues/17)) ([2c038ba](https://github.com/DatagridAI/datagrid-python/commit/2c038baf6e09ebd2c65630c242895b5bb585ccb7))
* go live ([#19](https://github.com/DatagridAI/datagrid-python/issues/19)) ([dfbc3ca](https://github.com/DatagridAI/datagrid-python/commit/dfbc3cae6a6602b39172c77d90dba5515e2e7e2b))
* **internal:** bump rye to 0.44.0 ([56f5b6e](https://github.com/DatagridAI/datagrid-python/commit/56f5b6efcc404937c2a2d586967709e147933cd5))
* **internal:** codegen related update ([9e57466](https://github.com/DatagridAI/datagrid-python/commit/9e57466158d9e16926d5edcb5c53054708631d60))
* **internal:** remove extra empty newlines ([b54de0b](https://github.com/DatagridAI/datagrid-python/commit/b54de0ba993ad58222df632eca3c8a754cd55efa))
* update SDK settings ([22cc8c2](https://github.com/DatagridAI/datagrid-python/commit/22cc8c239a282a07d2fdc2ef40f25e976ac8989a))
* update SDK settings ([#20](https://github.com/DatagridAI/datagrid-python/issues/20)) ([78e7524](https://github.com/DatagridAI/datagrid-python/commit/78e7524024c5c2b79b17d5d34338a8ae4b2ad179))


### Documentation

* revise readme docs about nested params ([868768f](https://github.com/DatagridAI/datagrid-python/commit/868768f89aa8aa8f169496404050b8a76aee397d))

## 0.1.0-alpha.6 (2025-04-03)

Full Changelog: [v0.1.0-alpha.5...v0.1.0-alpha.6](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.5...v0.1.0-alpha.6)

### Features

* **api:** api update ([1d75da9](https://github.com/DatagridAI/datagrid-python/commit/1d75da98c63d3280a3e03c76121d2fe6b07ce12f))
* **api:** api update ([60a4ca6](https://github.com/DatagridAI/datagrid-python/commit/60a4ca686fe70137e2bd7e2366fffc1823c6f49b))
* **api:** api update ([52939fd](https://github.com/DatagridAI/datagrid-python/commit/52939fdb8b703414efc1568bec0659ef23548d80))
* **api:** api update ([fb19d73](https://github.com/DatagridAI/datagrid-python/commit/fb19d73af6dcf03941d3866351c581f2cff2a5b4))
* **api:** api update ([93fb0d4](https://github.com/DatagridAI/datagrid-python/commit/93fb0d4e4e1dc6e5172429515e70aad79e0ad6e2))
* **api:** api update ([941cf45](https://github.com/DatagridAI/datagrid-python/commit/941cf4546e4878e8489756c98c2570c98f570f6c))
* **api:** api update ([66b6770](https://github.com/DatagridAI/datagrid-python/commit/66b6770bdde6d3a77ed50613b25fcb1fb33220d4))
* **api:** api update ([b5d6a8c](https://github.com/DatagridAI/datagrid-python/commit/b5d6a8ca109ee89ad067c52bc2a9742e77e438b8))
* **api:** manual updates ([97e0bd5](https://github.com/DatagridAI/datagrid-python/commit/97e0bd582eb2428bd0abd8423e8c90995b0654f8))
* **api:** manual updates ([2b17522](https://github.com/DatagridAI/datagrid-python/commit/2b17522f5b743047bba597447667fbdcd302fdf4))
* **api:** update via SDK Studio ([9b8b99d](https://github.com/DatagridAI/datagrid-python/commit/9b8b99de5655c824bba0cd1c39ebe86d111e7fda))
* **api:** update via SDK Studio ([4356f22](https://github.com/DatagridAI/datagrid-python/commit/4356f2273f8df43faa7e72caf384a717aeb11283))
* **client:** allow passing `NotGiven` for body ([80af128](https://github.com/DatagridAI/datagrid-python/commit/80af12839a681c57ffe197630d8909812d72aeec))
* **client:** send `X-Stainless-Read-Timeout` header ([9be674c](https://github.com/DatagridAI/datagrid-python/commit/9be674c4ae28023120412482e57f860622067800))
* sse converse ([d771e3b](https://github.com/DatagridAI/datagrid-python/commit/d771e3bbcbc2cf0be4f368d0d1ab56a523b88c81))
* sse converse ([d771e3b](https://github.com/DatagridAI/datagrid-python/commit/d771e3bbcbc2cf0be4f368d0d1ab56a523b88c81))
* support for SSE converse ([0e95ca4](https://github.com/DatagridAI/datagrid-python/commit/0e95ca428a7593a13a7be1f47256aef30ff9b3e9))


### Bug Fixes

* asyncify on non-asyncio runtimes ([18b81e5](https://github.com/DatagridAI/datagrid-python/commit/18b81e5b94d50c9ac1d221be9f960c719ea53fcf))
* **client:** mark some request bodies as optional ([80af128](https://github.com/DatagridAI/datagrid-python/commit/80af12839a681c57ffe197630d8909812d72aeec))
* **client:** only call .close() when needed ([49224f5](https://github.com/DatagridAI/datagrid-python/commit/49224f551ffa1cf522b8f915c0150f6b0ccec8b3))
* correctly handle deserialising `cls` fields ([4e06990](https://github.com/DatagridAI/datagrid-python/commit/4e06990be5b8fb76cad39b97dafb0a7b350c45f8))
* proper header ([710309f](https://github.com/DatagridAI/datagrid-python/commit/710309ffd9ed01d181d5d44368454d63c6285a7a))
* rm docstring from the overloaded def ([75b11ce](https://github.com/DatagridAI/datagrid-python/commit/75b11ceac6c49277ca3e0f51b9648d061077793c))
* tests ([94160e8](https://github.com/DatagridAI/datagrid-python/commit/94160e8dac5014ea368517637ad7180b0ed514f2))


### Chores

* **docs:** update client docstring ([cf00c67](https://github.com/DatagridAI/datagrid-python/commit/cf00c6780a611b64a4e6c275e1bf4090f7b8b04f))
* go live ([#1](https://github.com/DatagridAI/datagrid-python/issues/1)) ([b608c44](https://github.com/DatagridAI/datagrid-python/commit/b608c44014061206cd2a0b2023fd6fe715107bfb))
* go live ([#1](https://github.com/DatagridAI/datagrid-python/issues/1)) ([379ce7a](https://github.com/DatagridAI/datagrid-python/commit/379ce7a02b84a30151f647b86ff1ba94d6f1d695))
* go live ([#10](https://github.com/DatagridAI/datagrid-python/issues/10)) ([18e8a01](https://github.com/DatagridAI/datagrid-python/commit/18e8a0151ea1afa7724c82923cbde1639ecdd960))
* go live ([#12](https://github.com/DatagridAI/datagrid-python/issues/12)) ([2e31e51](https://github.com/DatagridAI/datagrid-python/commit/2e31e5110cb8a84952ded99e6a380a6cb7059b96))
* go live ([#14](https://github.com/DatagridAI/datagrid-python/issues/14)) ([377e546](https://github.com/DatagridAI/datagrid-python/commit/377e546829b09b4bae97dd31870639943577defb))
* go live ([#3](https://github.com/DatagridAI/datagrid-python/issues/3)) ([31dd324](https://github.com/DatagridAI/datagrid-python/commit/31dd324ceb90b1c9a7d546ed984bee88c5dbc1ca))
* go live ([#6](https://github.com/DatagridAI/datagrid-python/issues/6)) ([75ac964](https://github.com/DatagridAI/datagrid-python/commit/75ac96490178d1214d15741c9a12e2e3868b6703))
* **internal:** bummp ruff dependency ([f4eefdf](https://github.com/DatagridAI/datagrid-python/commit/f4eefdf62acaa67e3cdd64d7e9ae516ddf176546))
* **internal:** bump httpx dependency ([413952c](https://github.com/DatagridAI/datagrid-python/commit/413952c264538f97d317c95d87876cb058d64c8d))
* **internal:** change default timeout to an int ([359c23c](https://github.com/DatagridAI/datagrid-python/commit/359c23c3276a032c7ead84d44f61ead0ec22dd0d))
* **internal:** codegen related update ([3cd8e1a](https://github.com/DatagridAI/datagrid-python/commit/3cd8e1afe81e4c438b663a1022677045fa052cd8))
* **internal:** codegen related update ([b38e485](https://github.com/DatagridAI/datagrid-python/commit/b38e48539cf573deb543c5a4b3e1c9a001494c6b))
* **internal:** codegen related update ([8e61214](https://github.com/DatagridAI/datagrid-python/commit/8e61214d9e0c146005e00bf1dfdd3563af952acd))
* **internal:** codegen related update ([a2a5915](https://github.com/DatagridAI/datagrid-python/commit/a2a5915b64fc7c52da27ffb39f95d63e7b39e69c))
* **internal:** codegen related update ([e44f3ba](https://github.com/DatagridAI/datagrid-python/commit/e44f3ba933e4c22292f33126ffd804e7459c4331))
* **internal:** codegen related update ([31f7bfd](https://github.com/DatagridAI/datagrid-python/commit/31f7bfdeabb11f65d7c4c6548475b1a856147c11))
* **internal:** codegen related update ([6597ed4](https://github.com/DatagridAI/datagrid-python/commit/6597ed414dcb7e2a1bd03163f3bf26fa7d0ba27f))
* **internal:** fix devcontainers setup ([dce524c](https://github.com/DatagridAI/datagrid-python/commit/dce524c041c77b024e633443ba9e5acbc06b847b))
* **internal:** fix some typos ([d7bf113](https://github.com/DatagridAI/datagrid-python/commit/d7bf11367981380729d2eee052e0bcd5bc2c5837))
* **internal:** fix type traversing dictionary params ([1d381eb](https://github.com/DatagridAI/datagrid-python/commit/1d381ebfed07d84c9763ae80af19aa31ed39a35e))
* **internal:** minor formatting changes ([1608034](https://github.com/DatagridAI/datagrid-python/commit/16080345f25c83d34a2fbd2250741f061aedae6c))
* **internal:** minor type handling changes ([bd2ae66](https://github.com/DatagridAI/datagrid-python/commit/bd2ae6666eae680c0c26f05a91a7d6476541fb33))
* **internal:** properly set __pydantic_private__ ([e4b9ec6](https://github.com/DatagridAI/datagrid-python/commit/e4b9ec680aab049141b55110bc88bc22e8ee94cc))
* **internal:** remove unused http client options forwarding ([dadae7c](https://github.com/DatagridAI/datagrid-python/commit/dadae7c7cf6949c504bcdcb1fddb14945b1211b3))
* **internal:** update client tests ([08398a7](https://github.com/DatagridAI/datagrid-python/commit/08398a7439cc156a16a84d2e044864476fd05824))
* sync repo ([8397cc3](https://github.com/DatagridAI/datagrid-python/commit/8397cc34de7a7ba2ced88732507070148bd7921c))
* update SDK settings ([#3](https://github.com/DatagridAI/datagrid-python/issues/3)) ([dd5ded3](https://github.com/DatagridAI/datagrid-python/commit/dd5ded35ca67baa02693285fcde3f5ac85d8feee))
* update SDK settings ([#4](https://github.com/DatagridAI/datagrid-python/issues/4)) ([acd7f70](https://github.com/DatagridAI/datagrid-python/commit/acd7f70e749b1c9dad7df54fe1a1b64f4d42ffe8))
* update SDK settings ([#8](https://github.com/DatagridAI/datagrid-python/issues/8)) ([7370457](https://github.com/DatagridAI/datagrid-python/commit/7370457e992a180d2ea42d8499402e30b6d774b2))


### Documentation

* fix typos ([647dc35](https://github.com/DatagridAI/datagrid-python/commit/647dc35d4c22fcf7964b5df9e512b6213c6ed71b))
* **readme:** example snippet for client context manager ([34d4dc9](https://github.com/DatagridAI/datagrid-python/commit/34d4dc9bf14f6d6aef814c7055a415873bc3aef5))
* update URLs from stainlessapi.com to stainless.com ([85a7345](https://github.com/DatagridAI/datagrid-python/commit/85a73452c81fc9186bc48c1916f46f31a890ed04))

## 0.1.0-alpha.5 (2025-03-05)

Full Changelog: [v0.1.0-alpha.4...v0.1.0-alpha.5](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.4...v0.1.0-alpha.5)

### Features

* **api:** api update ([1d75da9](https://github.com/DatagridAI/datagrid-python/commit/1d75da98c63d3280a3e03c76121d2fe6b07ce12f))
* **api:** api update ([60a4ca6](https://github.com/DatagridAI/datagrid-python/commit/60a4ca686fe70137e2bd7e2366fffc1823c6f49b))
* **api:** api update ([52939fd](https://github.com/DatagridAI/datagrid-python/commit/52939fdb8b703414efc1568bec0659ef23548d80))
* **client:** allow passing `NotGiven` for body ([80af128](https://github.com/DatagridAI/datagrid-python/commit/80af12839a681c57ffe197630d8909812d72aeec))
* **client:** send `X-Stainless-Read-Timeout` header ([9be674c](https://github.com/DatagridAI/datagrid-python/commit/9be674c4ae28023120412482e57f860622067800))


### Bug Fixes

* asyncify on non-asyncio runtimes ([18b81e5](https://github.com/DatagridAI/datagrid-python/commit/18b81e5b94d50c9ac1d221be9f960c719ea53fcf))
* **client:** mark some request bodies as optional ([80af128](https://github.com/DatagridAI/datagrid-python/commit/80af12839a681c57ffe197630d8909812d72aeec))


### Chores

* **docs:** update client docstring ([cf00c67](https://github.com/DatagridAI/datagrid-python/commit/cf00c6780a611b64a4e6c275e1bf4090f7b8b04f))
* go live ([#14](https://github.com/DatagridAI/datagrid-python/issues/14)) ([377e546](https://github.com/DatagridAI/datagrid-python/commit/377e546829b09b4bae97dd31870639943577defb))
* **internal:** bummp ruff dependency ([f4eefdf](https://github.com/DatagridAI/datagrid-python/commit/f4eefdf62acaa67e3cdd64d7e9ae516ddf176546))
* **internal:** change default timeout to an int ([359c23c](https://github.com/DatagridAI/datagrid-python/commit/359c23c3276a032c7ead84d44f61ead0ec22dd0d))
* **internal:** fix devcontainers setup ([dce524c](https://github.com/DatagridAI/datagrid-python/commit/dce524c041c77b024e633443ba9e5acbc06b847b))
* **internal:** fix type traversing dictionary params ([1d381eb](https://github.com/DatagridAI/datagrid-python/commit/1d381ebfed07d84c9763ae80af19aa31ed39a35e))
* **internal:** minor type handling changes ([bd2ae66](https://github.com/DatagridAI/datagrid-python/commit/bd2ae6666eae680c0c26f05a91a7d6476541fb33))
* **internal:** properly set __pydantic_private__ ([e4b9ec6](https://github.com/DatagridAI/datagrid-python/commit/e4b9ec680aab049141b55110bc88bc22e8ee94cc))
* **internal:** remove unused http client options forwarding ([dadae7c](https://github.com/DatagridAI/datagrid-python/commit/dadae7c7cf6949c504bcdcb1fddb14945b1211b3))
* **internal:** update client tests ([08398a7](https://github.com/DatagridAI/datagrid-python/commit/08398a7439cc156a16a84d2e044864476fd05824))


### Documentation

* update URLs from stainlessapi.com to stainless.com ([85a7345](https://github.com/DatagridAI/datagrid-python/commit/85a73452c81fc9186bc48c1916f46f31a890ed04))

## 0.1.0-alpha.4 (2025-01-29)

Full Changelog: [v0.1.0-alpha.3...v0.1.0-alpha.4](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.3...v0.1.0-alpha.4)

### Features

* **api:** api update ([fb19d73](https://github.com/DatagridAI/datagrid-python/commit/fb19d73af6dcf03941d3866351c581f2cff2a5b4))


### Chores

* go live ([#10](https://github.com/DatagridAI/datagrid-python/issues/10)) ([18e8a01](https://github.com/DatagridAI/datagrid-python/commit/18e8a0151ea1afa7724c82923cbde1639ecdd960))
* go live ([#12](https://github.com/DatagridAI/datagrid-python/issues/12)) ([2e31e51](https://github.com/DatagridAI/datagrid-python/commit/2e31e5110cb8a84952ded99e6a380a6cb7059b96))
* sync repo ([8397cc3](https://github.com/DatagridAI/datagrid-python/commit/8397cc34de7a7ba2ced88732507070148bd7921c))

## 0.1.0-alpha.3 (2025-01-28)

Full Changelog: [v0.1.0-alpha.2...v0.1.0-alpha.3](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.2...v0.1.0-alpha.3)

### Chores

* go live ([#6](https://github.com/DatagridAI/datagrid-python/issues/6)) ([75ac964](https://github.com/DatagridAI/datagrid-python/commit/75ac96490178d1214d15741c9a12e2e3868b6703))
* update SDK settings ([#8](https://github.com/DatagridAI/datagrid-python/issues/8)) ([7370457](https://github.com/DatagridAI/datagrid-python/commit/7370457e992a180d2ea42d8499402e30b6d774b2))

## 0.1.0-alpha.2 (2025-01-27)

Full Changelog: [v0.1.0-alpha.1...v0.1.0-alpha.2](https://github.com/DatagridAI/datagrid-python/compare/v0.1.0-alpha.1...v0.1.0-alpha.2)

### Features

* **api:** api update ([93fb0d4](https://github.com/DatagridAI/datagrid-python/commit/93fb0d4e4e1dc6e5172429515e70aad79e0ad6e2))
* **api:** api update ([941cf45](https://github.com/DatagridAI/datagrid-python/commit/941cf4546e4878e8489756c98c2570c98f570f6c))
* **api:** api update ([66b6770](https://github.com/DatagridAI/datagrid-python/commit/66b6770bdde6d3a77ed50613b25fcb1fb33220d4))
* **api:** manual updates ([97e0bd5](https://github.com/DatagridAI/datagrid-python/commit/97e0bd582eb2428bd0abd8423e8c90995b0654f8))
* **api:** manual updates ([2b17522](https://github.com/DatagridAI/datagrid-python/commit/2b17522f5b743047bba597447667fbdcd302fdf4))
* sse converse ([d771e3b](https://github.com/DatagridAI/datagrid-python/commit/d771e3bbcbc2cf0be4f368d0d1ab56a523b88c81))
* sse converse ([d771e3b](https://github.com/DatagridAI/datagrid-python/commit/d771e3bbcbc2cf0be4f368d0d1ab56a523b88c81))
* support for SSE converse ([0e95ca4](https://github.com/DatagridAI/datagrid-python/commit/0e95ca428a7593a13a7be1f47256aef30ff9b3e9))


### Bug Fixes

* proper header ([710309f](https://github.com/DatagridAI/datagrid-python/commit/710309ffd9ed01d181d5d44368454d63c6285a7a))
* rm docstring from the overloaded def ([75b11ce](https://github.com/DatagridAI/datagrid-python/commit/75b11ceac6c49277ca3e0f51b9648d061077793c))
* tests ([94160e8](https://github.com/DatagridAI/datagrid-python/commit/94160e8dac5014ea368517637ad7180b0ed514f2))


### Chores

* go live ([#1](https://github.com/DatagridAI/datagrid-python/issues/1)) ([b608c44](https://github.com/DatagridAI/datagrid-python/commit/b608c44014061206cd2a0b2023fd6fe715107bfb))
* go live ([#3](https://github.com/DatagridAI/datagrid-python/issues/3)) ([31dd324](https://github.com/DatagridAI/datagrid-python/commit/31dd324ceb90b1c9a7d546ed984bee88c5dbc1ca))
* **internal:** codegen related update ([3cd8e1a](https://github.com/DatagridAI/datagrid-python/commit/3cd8e1afe81e4c438b663a1022677045fa052cd8))
* **internal:** minor formatting changes ([1608034](https://github.com/DatagridAI/datagrid-python/commit/16080345f25c83d34a2fbd2250741f061aedae6c))
* update SDK settings ([#4](https://github.com/DatagridAI/datagrid-python/issues/4)) ([acd7f70](https://github.com/DatagridAI/datagrid-python/commit/acd7f70e749b1c9dad7df54fe1a1b64f4d42ffe8))

## 0.1.0-alpha.1 (2025-01-15)

Full Changelog: [v0.0.1-alpha.0...v0.1.0-alpha.1](https://github.com/ToricLabs/datagrid-python/compare/v0.0.1-alpha.0...v0.1.0-alpha.1)

### Features

* **api:** api update ([b5d6a8c](https://github.com/ToricLabs/datagrid-python/commit/b5d6a8ca109ee89ad067c52bc2a9742e77e438b8))
* **api:** update via SDK Studio ([9b8b99d](https://github.com/ToricLabs/datagrid-python/commit/9b8b99de5655c824bba0cd1c39ebe86d111e7fda))
* **api:** update via SDK Studio ([4356f22](https://github.com/ToricLabs/datagrid-python/commit/4356f2273f8df43faa7e72caf384a717aeb11283))


### Bug Fixes

* **client:** only call .close() when needed ([49224f5](https://github.com/ToricLabs/datagrid-python/commit/49224f551ffa1cf522b8f915c0150f6b0ccec8b3))
* correctly handle deserialising `cls` fields ([4e06990](https://github.com/ToricLabs/datagrid-python/commit/4e06990be5b8fb76cad39b97dafb0a7b350c45f8))


### Chores

* go live ([#1](https://github.com/ToricLabs/datagrid-python/issues/1)) ([379ce7a](https://github.com/ToricLabs/datagrid-python/commit/379ce7a02b84a30151f647b86ff1ba94d6f1d695))
* **internal:** bump httpx dependency ([413952c](https://github.com/ToricLabs/datagrid-python/commit/413952c264538f97d317c95d87876cb058d64c8d))
* **internal:** codegen related update ([b38e485](https://github.com/ToricLabs/datagrid-python/commit/b38e48539cf573deb543c5a4b3e1c9a001494c6b))
* **internal:** codegen related update ([8e61214](https://github.com/ToricLabs/datagrid-python/commit/8e61214d9e0c146005e00bf1dfdd3563af952acd))
* **internal:** codegen related update ([a2a5915](https://github.com/ToricLabs/datagrid-python/commit/a2a5915b64fc7c52da27ffb39f95d63e7b39e69c))
* **internal:** codegen related update ([e44f3ba](https://github.com/ToricLabs/datagrid-python/commit/e44f3ba933e4c22292f33126ffd804e7459c4331))
* **internal:** codegen related update ([31f7bfd](https://github.com/ToricLabs/datagrid-python/commit/31f7bfdeabb11f65d7c4c6548475b1a856147c11))
* **internal:** codegen related update ([6597ed4](https://github.com/ToricLabs/datagrid-python/commit/6597ed414dcb7e2a1bd03163f3bf26fa7d0ba27f))
* **internal:** fix some typos ([d7bf113](https://github.com/ToricLabs/datagrid-python/commit/d7bf11367981380729d2eee052e0bcd5bc2c5837))
* update SDK settings ([#3](https://github.com/ToricLabs/datagrid-python/issues/3)) ([dd5ded3](https://github.com/ToricLabs/datagrid-python/commit/dd5ded35ca67baa02693285fcde3f5ac85d8feee))


### Documentation

* fix typos ([647dc35](https://github.com/ToricLabs/datagrid-python/commit/647dc35d4c22fcf7964b5df9e512b6213c6ed71b))
* **readme:** example snippet for client context manager ([34d4dc9](https://github.com/ToricLabs/datagrid-python/commit/34d4dc9bf14f6d6aef814c7055a415873bc3aef5))
