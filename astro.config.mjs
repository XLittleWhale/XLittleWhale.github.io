// astro.config.mjs
import { defineConfig } from 'astro/config';
import tailwindcss from '@tailwindcss/vite'; // 你之前用的是 v4 的配置

// 1. 引入数学插件
import remarkMath from 'remark-math';
import rehypeKatex from 'rehype-katex';

export default defineConfig({

  site: 'https://XLittleWhale.github.io',
  vite: {
    plugins: [tailwindcss()]
  },
  
  // 2. 配置 Markdown 处理
  markdown: {
    // 识别 $E=mc^2$ 语法
    remarkPlugins: [remarkMath],
    // 将其转换为 HTML
    rehypePlugins: [rehypeKatex],
  }
});