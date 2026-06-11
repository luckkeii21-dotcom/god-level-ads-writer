/* ===== shared vector helpers ===== */
const SVGNS='http://www.w3.org/2000/svg';
function E(n,a){const e=document.createElementNS(SVGNS,n);for(const k in a)e.setAttribute(k,a[k]);return e;}

/* Mechanical stopwatch whose hand points to `mark` (seconds on a 60 dial). */
function drawStopwatch(svg, mark){
  const cx=180, cy=250, R=150, ACCENT='#5aa600';
  const defs=E('defs',{});
  defs.innerHTML=`
    <linearGradient id="bezel" x1="0" y1="0" x2="1" y2="1">
      <stop offset="0" stop-color="#fbfdff"/><stop offset=".22" stop-color="#cfd6df"/>
      <stop offset=".46" stop-color="#9aa2ad"/><stop offset=".58" stop-color="#f2f5f8"/>
      <stop offset=".74" stop-color="#b3bbc5"/><stop offset="1" stop-color="#7e8691"/>
    </linearGradient>
    <radialGradient id="face" cx=".42" cy=".36" r=".75">
      <stop offset="0" stop-color="#f7f5ee"/><stop offset=".7" stop-color="#ece8da"/><stop offset="1" stop-color="#d3cdba"/>
    </radialGradient>
    <linearGradient id="crown" x1="0" y1="0" x2="1" y2="0">
      <stop offset="0" stop-color="#aeb6c0"/><stop offset=".5" stop-color="#f1f4f7"/><stop offset="1" stop-color="#8d949f"/>
    </linearGradient>`;
  svg.appendChild(defs);
  // crown + side button
  svg.appendChild(E('rect',{x:cx-15,y:40,width:30,height:34,rx:6,fill:'url(#crown)'}));
  svg.appendChild(E('rect',{x:cx-34,y:18,width:68,height:30,rx:14,fill:'url(#crown)',stroke:'#7c838d','stroke-width':1}));
  const sbx=cx+Math.cos(-Math.PI/4)*R, sby=cy+Math.sin(-Math.PI/4)*R;
  svg.appendChild(E('rect',{x:sbx-8,y:sby-26,width:30,height:24,rx:7,fill:'url(#crown)',stroke:'#7c838d','stroke-width':1,transform:`rotate(45 ${sbx} ${sby})`}));
  // body
  svg.appendChild(E('circle',{cx,cy,r:R,fill:'url(#bezel)'}));
  svg.appendChild(E('circle',{cx,cy,r:R-18,fill:'#8e95a0'}));
  svg.appendChild(E('circle',{cx,cy,r:R-22,fill:'url(#face)'}));
  // ticks
  const g=E('g',{});
  for(let i=0;i<60;i++){
    const a=(i/60)*2*Math.PI-Math.PI/2, major=i%5===0, r1=R-30, r2=R-(major?44:37);
    g.appendChild(E('line',{x1:cx+Math.cos(a)*r1,y1:cy+Math.sin(a)*r1,x2:cx+Math.cos(a)*r2,y2:cy+Math.sin(a)*r2,
      stroke:major?'#3c4047':'#9b9888','stroke-width':major?3.4:1.6,'stroke-linecap':'round'}));
  }
  svg.appendChild(g);
  // numerals (skip the one we highlight)
  [[15,'15'],[30,'30'],[45,'45'],[0,'60']].filter(([i])=>i!==mark).forEach(([i,t])=>{
    const a=(i/60)*2*Math.PI-Math.PI/2, rr=R-64;
    const tx=E('text',{x:cx+Math.cos(a)*rr,y:cy+Math.sin(a)*rr,fill:'#54585f','font-size':18,'font-family':'Inter, sans-serif','font-weight':600,'text-anchor':'middle','dominant-baseline':'central'});
    tx.textContent=t; svg.appendChild(tx);
  });
  // highlighted mark numeral + tick
  (function(){
    const a=(mark/60)*2*Math.PI-Math.PI/2;
    g.appendChild(E('line',{x1:cx+Math.cos(a)*(R-30),y1:cy+Math.sin(a)*(R-30),x2:cx+Math.cos(a)*(R-46),y2:cy+Math.sin(a)*(R-46),stroke:ACCENT,'stroke-width':4.6,'stroke-linecap':'round'}));
    const rr=R-64, tx=E('text',{x:cx+Math.cos(a)*rr,y:cy+Math.sin(a)*rr,fill:ACCENT,'font-size':23,'font-family':'Inter, sans-serif','font-weight':800,'text-anchor':'middle','dominant-baseline':'central'});
    tx.textContent=String(mark); svg.appendChild(tx);
  })();
  // accent sweep 0 -> mark
  (function(){
    const rr=R-30, a0=-Math.PI/2, a1=(mark/60)*2*Math.PI-Math.PI/2;
    const big=(mark/60)>0.5?1:0;
    svg.appendChild(E('path',{d:`M ${cx+Math.cos(a0)*rr} ${cy+Math.sin(a0)*rr} A ${rr} ${rr} 0 ${big} 1 ${cx+Math.cos(a1)*rr} ${cy+Math.sin(a1)*rr}`,
      stroke:ACCENT,'stroke-width':6,fill:'none','stroke-linecap':'round'}));
    svg.appendChild(E('circle',{cx:cx+Math.cos(a0)*rr,cy:cy+Math.sin(a0)*rr,r:4.5,fill:ACCENT}));
  })();
  // hand to mark
  (function(){
    const a=((mark/60)*360-90)*Math.PI/180, len=122, back=26;
    svg.appendChild(E('line',{x1:cx-Math.cos(a)*back,y1:cy-Math.sin(a)*back,x2:cx+Math.cos(a)*len,y2:cy+Math.sin(a)*len,stroke:'#2b2f36','stroke-width':5,'stroke-linecap':'round'}));
  })();
  svg.appendChild(E('circle',{cx,cy,r:11,fill:'#22262c'}));
  svg.appendChild(E('circle',{cx,cy,r:4.4,fill:ACCENT}));
}

/* Symmetric hand-drawn marker ellipse with a small gap at the top. */
function drawRing(pathEl, color, rot){
  const cx=500, cy=170, rx=470, ry=150, gap=13*Math.PI/180;
  const S=[cx+rx*Math.sin(gap), cy-ry*Math.cos(gap)], En=[cx-rx*Math.sin(gap), cy-ry*Math.cos(gap)];
  pathEl.setAttribute('d',`M ${S[0].toFixed(1)} ${S[1].toFixed(1)} A ${rx} ${ry} 0 1 1 ${En[0].toFixed(1)} ${En[1].toFixed(1)}`);
  pathEl.setAttribute('stroke',color); pathEl.setAttribute('stroke-width','10');
  pathEl.setAttribute('stroke-linecap','round'); pathEl.setAttribute('fill','none');
  if(pathEl.parentElement) pathEl.parentElement.setAttribute('transform',`rotate(${rot||-2})`);
}
