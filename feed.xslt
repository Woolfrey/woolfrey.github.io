<?xml version="1.0" encoding="UTF-8"?>
<xsl:stylesheet version="1.0"
  xmlns:xsl="http://www.w3.org/1999/XSL/Transform"
  xmlns:atom="http://www.w3.org/2005/Atom"
  exclude-result-prefixes="atom">

  <xsl:output method="html" version="1.0" encoding="UTF-8" indent="yes"/>

  <xsl:template match="/atom:feed">
    <html lang="en">
      <head>
        <meta charset="utf-8"/>
        <meta name="viewport" content="width=device-width, initial-scale=1"/>
        <title><xsl:value-of select="atom:title"/></title>
        <style>
          body {
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Helvetica, Arial, sans-serif;
            max-width: 40rem;
            margin: 2rem auto;
            padding: 0 1.25rem;
            color: #222;
            line-height: 1.5;
          }
          .feed-banner {
            background: #fdf6e3;
            border: 1px solid #eee0b7;
            border-radius: 6px;
            padding: 1rem 1.25rem;
            margin-bottom: 2rem;
            font-size: 0.95em;
          }
          .feed-banner p {
            margin: 0.4rem 0;
          }
          .feed-banner a {
            color: #b8860b;
            font-weight: 600;
          }
          h1 {
            font-size: 1.5em;
            margin-bottom: 0.25rem;
          }
          .feed-desc {
            color: #666;
            margin-top: 0;
            margin-bottom: 2rem;
          }
          .entry {
            padding: 1rem 0;
            border-bottom: 1px solid #eaeaea;
          }
          .entry:last-child {
            border-bottom: none;
          }
          .entry-date {
            font-size: 0.85em;
            color: #888;
            font-variant-numeric: tabular-nums;
          }
          .entry-title {
            margin: 0.2rem 0 0.3rem 0;
            font-size: 1.1em;
          }
          .entry-title a {
            color: #1a5490;
            text-decoration: none;
          }
          .entry-title a:hover {
            text-decoration: underline;
          }
        </style>
      </head>
      <body>
        <div class="feed-banner">
          <p><strong>This is a web feed</strong>, also known as an RSS/Atom feed. It isn't a normal webpage &#8212; it's meant to be read by a newsreader app, which checks it for new posts automatically.</p>
          <p>To subscribe: copy the URL from your browser's address bar and paste it into a newsreader such as <a href="https://feedly.com" target="_blank">Feedly</a>, <a href="https://www.inoreader.com" target="_blank">Inoreader</a>, or <a href="https://netnewswire.com" target="_blank">NetNewsWire</a>. New to feeds? See <a href="https://aboutfeeds.com" target="_blank">aboutfeeds.com</a> for a quick primer.</p>
          <p>Prefer email instead? <a href="/">Subscribe by email on the homepage</a>.</p>
        </div>

        <h1><xsl:value-of select="atom:title"/></h1>
        <xsl:if test="atom:subtitle">
          <p class="feed-desc"><xsl:value-of select="atom:subtitle"/></p>
        </xsl:if>

        <xsl:for-each select="atom:entry">
          <div class="entry">
            <div class="entry-date">
              <xsl:value-of select="substring(atom:published, 1, 10)"/>
            </div>
            <h2 class="entry-title">
              <a>
                <xsl:attribute name="href">
                  <xsl:value-of select="atom:link/@href"/>
                </xsl:attribute>
                <xsl:value-of select="atom:title"/>
              </a>
            </h2>
          </div>
        </xsl:for-each>
      </body>
    </html>
  </xsl:template>

</xsl:stylesheet>
