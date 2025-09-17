import { defineConfig } from "tsup";

export default defineConfig({
    entry: ["src/index.ts"],
    format: ["cjs", "esm"],
    dts: true,
    //outDir: "dist/bundle",
    outExtension({format}){
        return format === "cjs" ? {js: ".cjs"} : {js: ".mjs"};
    },
});