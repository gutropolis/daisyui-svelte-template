import type { CodegenConfig } from '@graphql-codegen/cli';

const config: CodegenConfig = {
	schema: 'http://localhost:8000/graphql',
	documents: ['src/**/*.{ts,svelte}'],
	generates: {
		'src/lib/graphql/generated.ts': {
			preset: 'client',
			plugins: ['typescript', 'typescript-operations'],
			config: {
				useTypeImports: true,
				avoidOptionals: false,
				scalars: {
					DateTime: 'Date'
				}
			}
		}
	}
};

export default config;
