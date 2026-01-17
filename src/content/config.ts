// src/content/config.ts
import { defineCollection, z } from 'astro:content';

// 1. 你的博客集合 (保持不变)
const blogCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    date: z.date(),
    description: z.string().optional(),
    tags: z.array(z.string()).optional(),
  }),
});

// 2. [新增] Research 集合
const researchCollection = defineCollection({
  type: 'content',
  schema: z.object({
    title: z.string(),
    description: z.string(), // 简短介绍，显示在卡片上
    date: z.date(),          // 项目开始时间或发布时间
    cover: z.string(),       // 封面图路径 (例如 /images/research-1.jpg)
    status: z.string().optional(), // 选填: "Ongoing", "Published", "Completed"
    venue: z.string().optional(),  // 选填: 发表在哪个会议/期刊
  }),
});

// 3. 导出所有集合
export const collections = {
  'blog': blogCollection,
  'research': researchCollection, // <--- 别忘了加上这个
};