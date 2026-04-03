---
layout: default
title: "치지직 채팅 분석기 - 채팅 급증 구간 자동 감지 Chrome 확장 프로그램"
description: "치지직 VOD·라이브 시청 중 채팅이 폭발하는 구간을 자동으로 찾아주는 Chrome 확장 프로그램. Z-Score 알고리즘으로 치지직 채팅 스파이크를 감지하고 편집 포인트를 제공합니다."
keywords: "치지직 채팅 분석기, 치지직 채팅, chzzk, 치지직 하이라이트, 치지직 편집, 채팅 급증, 채팅 스파이크, Chrome 확장 프로그램, 크롬 확장 프로그램"
permalink: /chzzk-chat-analyzer/
---

<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "SoftwareApplication",
  "name": "치지직 채팅 분석기",
  "alternateName": ["Chzzk Chat Analyzer", "chzzk-chat-analyzer"],
  "description": "치지직 VOD·라이브 시청 중 채팅이 폭발하는 구간을 자동으로 찾아주는 Chrome 확장 프로그램. Z-Score 통계 알고리즘으로 채팅 스파이크 구간을 감지하고 편집 포인트를 제공합니다.",
  "applicationCategory": "BrowserApplication",
  "operatingSystem": "Chrome",
  "url": "https://minthug.github.io/chzzk-chat-analyzer/",
  "downloadUrl": "https://chromewebstore.google.com/detail/chzzk-chat-analyzer/ghcibmmolpjfkjfhhfgjjfhfijbmaofj",
  "author": {
    "@type": "Person",
    "name": "minthug",
    "url": "https://minthug.github.io"
  },
  "offers": {
    "@type": "Offer",
    "price": "0",
    "priceCurrency": "KRW"
  },
  "screenshot": "https://minthug.github.io/assets/images/chzzk-chat-analyzer-screenshot.png",
  "featureList": [
    "치지직 채팅 급증 구간 자동 감지",
    "Z-Score 통계 알고리즘 기반 스파이크 분석",
    "재생바 위 채팅량 오버레이 그래프",
    "키워드 급증 구간 추적",
    "TXT·CSV 내보내기",
    "VOD·라이브 모두 지원"
  ],
  "keywords": "치지직, 치지직 채팅, chzzk, 채팅 분석, 하이라이트, 편집 포인트"
}
</script>

<div class="chzzk-landing">

  <div class="chzzk-hero">
    <h1 class="chzzk-hero-title">치지직 채팅 분석기</h1>
    <p class="chzzk-hero-subtitle">치지직 VOD·라이브의 <strong>채팅 폭발 구간</strong>을 자동으로 찾아주는 Chrome 확장 프로그램</p>
    <div class="chzzk-hero-actions">
      <a href="https://chromewebstore.google.com/detail/chzzk-chat-analyzer/ghcibmmolpjfkjfhhfgjjfhfijbmaofj"
         class="chzzk-btn chzzk-btn--primary" target="_blank" rel="noopener">
        Chrome 웹 스토어에서 설치
      </a>
      <a href="https://github.com/Minthug/chzzk-chat-analyzer"
         class="chzzk-btn chzzk-btn--secondary" target="_blank" rel="noopener">
        GitHub 소스 보기
      </a>
    </div>
  </div>

  <div class="chzzk-section">
    <h2>치지직 채팅 분석기란?</h2>
    <p>
      <strong>치지직 채팅 분석기</strong>는 치지직(CHZZK) 플랫폼의 VOD나 라이브 방송을 시청할 때,
      <strong>채팅이 갑자기 폭발적으로 증가하는 구간</strong>을 자동으로 감지해 알려주는 크롬 확장 프로그램입니다.
    </p>
    <p>
      영상 편집자, 콘텐츠 크리에이터, 혹은 긴 VOD에서 재밌는 장면만 빠르게 찾고 싶은 시청자 모두에게 유용합니다.
      치지직 채팅 데이터를 실시간으로 분석해 <strong>하이라이트 구간</strong>과 <strong>편집 포인트</strong>를 제공합니다.
    </p>
  </div>

  <div class="chzzk-section">
    <h2>주요 기능</h2>
    <div class="chzzk-features">

      <div class="chzzk-feature-card">
        <div class="chzzk-feature-icon">📈</div>
        <h3>치지직 채팅 스파이크 자동 감지</h3>
        <p>
          Z-Score 통계 알고리즘을 활용해 치지직 채팅이 급격히 증가하는 구간을 자동으로 탐지합니다.
          상위 3개 스파이크 구간을 ★로 하이라이트해 편집 포인트를 바로 확인할 수 있습니다.
        </p>
      </div>

      <div class="chzzk-feature-card">
        <div class="chzzk-feature-icon">🎬</div>
        <h3>채팅량 오버레이 그래프</h3>
        <p>
          치지직 재생바 위에 채팅량 곡선을 실시간으로 렌더링합니다.
          그래프의 특정 지점을 클릭하면 해당 시점으로 바로 이동할 수 있어 빠른 탐색이 가능합니다.
        </p>
      </div>

      <div class="chzzk-feature-card">
        <div class="chzzk-feature-icon">🔍</div>
        <h3>치지직 키워드 감지</h3>
        <p>
          특정 키워드(예: "ㅋㅋㅋ", "와", "대박")가 급증하는 구간을 별도로 추적합니다.
          치지직 채팅 데이터를 TXT 또는 CSV 형식으로 내보낼 수 있습니다.
        </p>
      </div>

      <div class="chzzk-feature-card">
        <div class="chzzk-feature-icon">🔴</div>
        <h3>VOD · 라이브 모두 지원</h3>
        <p>
          치지직 VOD 다시보기뿐만 아니라 라이브 방송 중에도 실시간으로 채팅 분석이 동작합니다.
        </p>
      </div>

    </div>
  </div>

  <div class="chzzk-section">
    <h2>이런 분들에게 유용합니다</h2>
    <ul class="chzzk-use-cases">
      <li><strong>치지직 영상 편집자</strong> — 긴 VOD에서 편집 포인트를 빠르게 찾고 싶을 때</li>
      <li><strong>치지직 콘텐츠 크리에이터</strong> — 내 방송의 하이라이트 구간을 파악하고 싶을 때</li>
      <li><strong>치지직 시청자</strong> — 놓친 라이브의 재밌는 순간만 골라서 보고 싶을 때</li>
      <li><strong>치지직 클립 제작자</strong> — 반응이 폭발한 구간을 자동으로 찾고 싶을 때</li>
    </ul>
  </div>

  <div class="chzzk-section">
    <h2>설치 방법</h2>
    <ol class="chzzk-steps">
      <li>아래 버튼을 클릭해 Chrome 웹 스토어로 이동합니다.</li>
      <li>"Chrome에 추가" 버튼을 클릭해 확장 프로그램을 설치합니다.</li>
      <li>치지직(chzzk.naver.com)에서 VOD나 라이브를 재생합니다.</li>
      <li>재생바 위에 채팅량 그래프가 자동으로 표시됩니다.</li>
    </ol>
    <a href="https://chromewebstore.google.com/detail/chzzk-chat-analyzer/ghcibmmolpjfkjfhhfgjjfhfijbmaofj"
       class="chzzk-btn chzzk-btn--primary" target="_blank" rel="noopener">
      무료로 설치하기 (Chrome 웹 스토어)
    </a>
  </div>

  <div class="chzzk-section">
    <h2>개발 배경</h2>
    <p>
      치지직에서 긴 VOD를 편집할 때, 어느 구간이 반응이 좋았는지 직접 전부 시청하며 찾아야 하는 불편함이 있었습니다.
      <strong>치지직 채팅 분석기</strong>는 이 문제를 해결하기 위해 만들었습니다.
      통계적 이상치 탐지(Z-Score)를 활용해 채팅이 급격히 늘어나는 구간, 즉 시청자들이 가장 열정적으로 반응한 순간을 자동으로 찾아냅니다.
    </p>
    <p>
      치지직 채팅 분석기는 오픈소스로 개발되었으며, 누구나 GitHub에서 소스를 확인하고 기여할 수 있습니다.
    </p>
    <a href="https://github.com/Minthug/chzzk-chat-analyzer"
       class="chzzk-btn chzzk-btn--secondary" target="_blank" rel="noopener">
      GitHub에서 소스 보기
    </a>
  </div>

</div>

<style>
.chzzk-landing { max-width: 800px; margin: 0 auto; padding: 2rem 1rem; color: #e6edf3; }
.chzzk-hero { text-align: center; padding: 3rem 0 2rem; }
.chzzk-hero-title { font-size: 2.2rem; font-weight: 700; margin-bottom: 1rem; color: #e6edf3; }
.chzzk-hero-subtitle { font-size: 1.1rem; color: #8b949e; margin-bottom: 2rem; }
.chzzk-hero-actions { display: flex; gap: 1rem; justify-content: center; flex-wrap: wrap; }
.chzzk-btn { display: inline-block; padding: .6rem 1.4rem; border-radius: 6px; font-size: .9rem; font-weight: 600; text-decoration: none; transition: opacity .15s; }
.chzzk-btn--primary { background: #238636; color: #fff; border: 1px solid #2ea043; }
.chzzk-btn--primary:hover { opacity: .85; }
.chzzk-btn--secondary { background: #21262d; color: #c9d1d9; border: 1px solid #30363d; }
.chzzk-btn--secondary:hover { background: #30363d; }
.chzzk-section { margin: 2.5rem 0; }
.chzzk-section h2 { font-size: 1.3rem; font-weight: 600; border-bottom: 1px solid #30363d; padding-bottom: .5rem; margin-bottom: 1rem; }
.chzzk-section p, .chzzk-section li { color: #8b949e; line-height: 1.7; }
.chzzk-section strong { color: #e6edf3; }
.chzzk-features { display: grid; grid-template-columns: repeat(auto-fit, minmax(340px, 1fr)); gap: 1rem; }
.chzzk-feature-card { background: #161b22; border: 1px solid #30363d; border-radius: 8px; padding: 1.2rem; }
.chzzk-feature-card h3 { font-size: 1rem; margin: .5rem 0; color: #e6edf3; }
.chzzk-feature-card p { font-size: .9rem; margin: 0; }
.chzzk-feature-icon { font-size: 1.5rem; }
.chzzk-use-cases { padding-left: 1.5rem; }
.chzzk-use-cases li { margin-bottom: .5rem; }
.chzzk-steps { padding-left: 1.5rem; margin-bottom: 1.5rem; }
.chzzk-steps li { margin-bottom: .5rem; }
</style>
