const expectedTypes = ['feat', 'fix', 'test', 'build', 'refactor', 'docs'];

module.exports = {
  extends: ['@commitlint/config-conventional'],
  plugins: [
    {
      rules: {
        'custom-type-enum': ({ type }) => {
          if (!expectedTypes.includes(type)) {
            return [false,
              `
Commit message must be in the following format:\n

"type(scope): subject"\n

- Scope must be a Scaleway product acronym.\n

- Type must be one of the following:\n
${expectedTypes.join(', ')} \n

Example: 
"docs(INS): add new documentation page"
              `];
          }
          return [true];
        },
      },
    },
  ],
  rules: {
    'custom-type-enum': [2, 'always'],
  },
};
