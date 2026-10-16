export default function FooterSnippet({ tag }) {
  const src = process.env.HUMA_SOURCE_LINK || "https://github.com/kulup-org/plane-huma";
  return (
    <footer>
      <a href={src}>Kaynak Kodu (AGPL)</a>
      <span>{tag || process.env.HUMA_DEPLOY_TAG || "v1.3.0"}</span>
    </footer>
  );
}
