// Streaming Chat Completions with the OpenAI Node SDK.
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.outrun.to/v1",
  apiKey: process.env.OUTRUN_API_KEY,
  maxRetries: 0,
});

const stream = await client.chat.completions.create({
  model: "gpt-5.6-sol",
  messages: [{ role: "user", content: "Count to five, one number per line." }],
  stream: true,
});
for await (const chunk of stream) {
  process.stdout.write(chunk.choices[0]?.delta?.content ?? "");
}
process.stdout.write("\n");
