// Chat Completions with the official OpenAI Node SDK.
//   npm install
//   export OUTRUN_API_KEY="your-key"
//   node chat.mjs
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.outrun.to/v1",
  apiKey: process.env.OUTRUN_API_KEY,
  maxRetries: 0, // requests are billed; check Activity before retrying by hand
});

const resp = await client.chat.completions.create({
  model: "gpt-5.6-sol", // any text model ID from CATALOG.md
  messages: [
    { role: "system", content: "You are a helpful assistant." },
    { role: "user", content: "Say hello in five words." },
  ],
  max_tokens: 64,
});
console.log(resp.choices[0].message.content);
console.log(resp.usage);
