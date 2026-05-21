<template>
  <div class="page-container">
    <div class="guide-hero">
      <h1>欢迎来到拼豆的世界 🎈</h1>
      <p>在这里，我们帮你度过新手期，解答你关于制作过程中的一切疑问。</p>
    </div>

    <div class="guide-grid">
      <div class="guide-card">
        <h3>“什么是 5mm 豆和 2.6mm 豆？”</h3>
        <p>拼豆主要分为以下两个规格：</p>
        <ul>
          <li><strong>5mm 大豆</strong>：适合儿童和刚入门的新手。体积大，易于夹取，非常适合用来制作杯垫、大号立牌等大颗粒感、厚实的作品。</li>
          <li><strong>2.6mm 迷你豆</strong>：适合进阶手艺人和成年玩家。豆子极其迷你，需要配合专用细头镊子。它的细节表现力极强，能完美还原相片级的复杂图纸。</li>
        </ul>
      </div>

      <div class="guide-card">
        <h3>“熨斗怎么用才不会毁掉作品？”</h3>
        <p>熨烫决定成败，请熟记以下保姆级守则：</p>
        <ul>
          <li>1. 拼好后必须覆盖一层专用的<strong>助烫纸/助烫片</strong>，不可将熨斗直接接触未保护的豆子。</li>
          <li>2. 熨斗开至中温（去水汽，140℃ 左右），在作品上方贴紧并<strong>缓慢打圈</strong>移动，切忌在某一点停留过久。</li>
          <li>3. 观察透光度，当看到豆子中心孔径轻微收缩、粘合时即可。</li>
          <li>4. 翻面后再覆盖一张纸轻轻熨烫另一面。出锅后立刻压上重物冷却，防止翘曲。</li>
        </ul>
      </div>

      <div class="guide-card">
        <h3>🗺️ “如何看懂本站的导出图纸？”</h3>
        <p>为了让女生在买豆、拼豆时绝不看花眼，我们进行了深度定制：</p>
        <ul>
          <li><strong>A1、B2 坐标定位</strong>：导出的 PDF 顶端和左侧有像 Excel 一样的行列标识（A-Z, 1-100），方便对照找位置。</li>
          <li><strong>分块模板图纸</strong>：大尺寸图纸会自动分割为 29x29 大小的子拼图块，确保在一张小模板板上就能轻松对齐拼完。</li>
          <li><strong>防呆色卡购物单</strong>：末尾有一页专门对应各主流品牌的色号及颗粒数量，自带打钩选框。</li>
        </ul>
      </div>
    </div>
  </div>
</template>

<style scoped>
.page-container { max-width: 800px; margin: 0 auto; padding-left: 20px; padding-right: 20px; }

.guide-hero {
  background: var(--primary); color: white; padding: 40px;
  border-radius: var(--radius-lg); text-align: center; margin-bottom: 30px;
}
.guide-hero h1 { color: white; margin-bottom: 10px; font-weight: 900; }
.guide-hero p { color: white; opacity: 0.9; }

.guide-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 25px; }

.guide-card {
  background: white; padding: 30px; border-radius: var(--radius-md);
  box-shadow: var(--shadow-soft); border: 1px solid var(--border-color);
}
.guide-card h3 {
  display: flex; align-items: center; gap: 10px; margin-bottom: 15px;
  font-size: 18px; border-bottom: 2px dashed var(--border-color);
  padding-bottom: 12px; font-weight: 900;
}
.guide-card p, .guide-card li {
  font-size: 14px; line-height: 1.7; color: var(--text-main);
  margin-bottom: 10px; opacity: 0.9;
}
.guide-card ul { padding-left: 20px; }
</style>
