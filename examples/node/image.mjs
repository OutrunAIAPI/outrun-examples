// Generate one image and save it as image.png. Billed per image; no automatic retry.
import { writeFileSync } from "node:fs";
import OpenAI from "openai";

const client = new OpenAI({
  baseURL: "https://api.outrun.to/v1",
  apiKey: process.env.OUTRUN_API_KEY,
  maxRetries: 0,
});

const result = await client.images.generate({
  model: "gemini-3-pro-image", // or gemini-3.1-flash-image, gpt-image-2, grok-imagine-image
  prompt: "A lighthouse at dawn, oil painting",
  size: "16:9",
});
writeFileSync("image.png", Buffer.from(result.data[0].b64_json, "base64"));
console.log("Saved image.png");
