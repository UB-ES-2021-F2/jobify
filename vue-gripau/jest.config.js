module.exports = {
  preset: '@vue/cli-plugin-unit-jest/presets/no-babel',
  collectCoverage: true,
  collectCoverageFrom: ['src/components/*'],
  // set the value to the custom resolver created in step 1
  resolver: "<rootDir>/tests/unit/my-module-resolve.js",
  // browser bundles in firebase are ESM, transform them to CJS to work in Jest
  transformIgnorePatterns: [
    "<rootDir>/node_modules/(?!(@firebase.*)/)"
  ]
}
