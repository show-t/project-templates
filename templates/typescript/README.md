# TypeScript Template

A minimal TypeScript project template for Node.js or frontend development

## 📦 Features

- TypeScript 5.x
- ESM (`module: nodenext`)
- Strict type checking
- Declaration file generation
- Ready for use with `pnpm`

## 📚 Requirements

- Node.js >= 18
- pnpm >= 8

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/show-t/typescript-template.git
cd typescript-template
```

### 2. Install dependencies

```bash
pnpm install
```

### 3. Build the project

```bash
pnpm build
```

### 4. Run the output

```bash
pnpm start
```

## 🛠️ Scripts

| Command         | Description                     |
|-----------------|---------------------------------|
| `pnpm build`    | Compile TypeScript to `build/`  |
| `pnpm bundle`   | Bundle the source file          |
| `pnpm dev`      | Run the app in development mode |
| `pnpm dev:watch`| Run the app in watch mode       |
| `pnpm start`    | Run compiled code with Node.js  |
| `pnpm cls:build`| Remove `build/` directory       |
| `pnpm cls:dist` | Remove `dist/` directory        |

## 📁 Project Structure

```
.
├── src/            # TypeScript source files
│   └── index.ts
├── dist/           # Compiled JavaScript output
├── tsconfig.json   # TypeScript configuration
├── package.json    # Project metadata and scripts
├── .gitignore   
├── LICENSE   
└── README.md       # Project documentation
```

## 📄 License

This project is licensed under the MIT License.
See the [LICENSE](./LICENSE) file for more details.