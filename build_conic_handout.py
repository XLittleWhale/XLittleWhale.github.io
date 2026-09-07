from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.units import mm
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, PageBreak, Table, TableStyle, KeepTogether
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen.canvas import Canvas

OUT = "output/pdf/圆锥曲线几何关系讲义.pdf"
pdfmetrics.registerFont(TTFont("Chinese", "/System/Library/Fonts/STHeiti Medium.ttc", subfontIndex=0))

PAGE_W, PAGE_H = A4
BLUE = colors.HexColor("#1F4E79")
LIGHT = colors.HexColor("#EAF2F8")
GRAY = colors.HexColor("#555555")

styles = getSampleStyleSheet()
styles.add(ParagraphStyle(name="CNTitle", fontName="Chinese", fontSize=22, leading=30, alignment=TA_CENTER, textColor=BLUE, spaceAfter=10))
styles.add(ParagraphStyle(name="CNSub", fontName="Chinese", fontSize=10.5, leading=18, alignment=TA_CENTER, textColor=GRAY, spaceAfter=12))
styles.add(ParagraphStyle(name="CNH1", fontName="Chinese", fontSize=15, leading=22, textColor=BLUE, spaceBefore=4, spaceAfter=8))
styles.add(ParagraphStyle(name="CNH2", fontName="Chinese", fontSize=12, leading=19, textColor=colors.HexColor("#2F5597"), spaceBefore=5, spaceAfter=4))
styles.add(ParagraphStyle(name="CNBody", fontName="Chinese", fontSize=10.2, leading=17, textColor=colors.HexColor("#222222"), spaceAfter=5))
styles.add(ParagraphStyle(name="CNSmall", fontName="Chinese", fontSize=9, leading=14, textColor=GRAY, spaceAfter=4))
styles.add(ParagraphStyle(name="Eq", fontName="Chinese", fontSize=11, leading=18, alignment=TA_CENTER, textColor=colors.HexColor("#111111"), spaceBefore=4, spaceAfter=7))
styles.add(ParagraphStyle(name="Box", fontName="Chinese", fontSize=10, leading=17, leftIndent=8, rightIndent=8, textColor=colors.HexColor("#163A5F"), spaceBefore=4, spaceAfter=7))

def P(text, style="CNBody"):
    return Paragraph(text, styles[style])

def E(text):
    return Paragraph(text, styles["Eq"])

def box(text):
    t = Table([[P(text, "Box")]], colWidths=[170*mm])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0,0), (-1,-1), LIGHT),
        ("BOX", (0,0), (-1,-1), 0.6, colors.HexColor("#9CC2E5")),
        ("LEFTPADDING", (0,0), (-1,-1), 5),
        ("RIGHTPADDING", (0,0), (-1,-1), 5),
        ("TOPPADDING", (0,0), (-1,-1), 4),
        ("BOTTOMPADDING", (0,0), (-1,-1), 4),
    ]))
    return t

def header_footer(canvas: Canvas, doc):
    canvas.saveState()
    canvas.setStrokeColor(colors.HexColor("#D9E2F3"))
    canvas.line(18*mm, PAGE_H-15*mm, PAGE_W-18*mm, PAGE_H-15*mm)
    canvas.setFont("Chinese", 8)
    canvas.setFillColor(GRAY)
    canvas.drawString(18*mm, PAGE_H-11*mm, "圆锥曲线中的几何关系")
    canvas.drawRightString(PAGE_W-18*mm, 10*mm, f"第 {doc.page} 页")
    canvas.restoreState()

story = []
story += [P("圆锥曲线中的几何关系", "CNTitle"),
          P("从二次方程的根，到焦点、准线、渐近线与调和关系", "CNSub"),
          box("核心想法：把直线与圆锥曲线的交点用一个参数表示。代入后得到二次方程；交点的和、积、重合，分别对应韦达定理、长度积和切线。涉及焦点准线时用距离，涉及调和关系时用交比。"),
          P("一、直线截圆锥曲线：所有题的出发点", "CNH1"),
          P("设圆锥曲线为", "CNBody"),
          E("F(x,y)=Ax²+Bxy+Cy²+Dx+Ey+F₀=0"),
          P("取一条直线，并用参数 t 表示：", "CNBody"),
          E("(x,y)=(x₀,y₀)+t(u,v)"),
          P("代入后必然得到关于 t 的二次方程", "CNBody"),
          E("αt²+βt+γ=0"),
          P("若两个交点对应的参数为 t₁,t₂，则由韦达定理", "CNBody"),
          E("t₁+t₂=-β/α，　t₁t₂=γ/α"),
          box("因此，求两个交点的坐标通常不是最好的第一步。先研究参数的和、积和是否重合，往往可以直接得到结论。"),
          P("二、长度积：把距离变成根的乘积", "CNH1"),
          P("如果直线方向向量 (u,v) 是单位向量，且定点 P 对应 t=0，那么", "CNBody"),
          E("|PM|=|t₁|，　|PN|=|t₂|"),
          E("|PM|·|PN|=|t₁t₂|=|γ/α|"),
          P("其中 γ=F(P)，只由定点 P 决定；α 是二次项沿直线方向的值。", "CNBody"),
          P("对椭圆 x²/a²+y²/b²=1，若方向单位向量为 (u,v)，则", "CNBody"),
          E("α=u²/a²+v²/b²"),
          P("当 a>b>0 时", "CNBody"),
          E("1/a² ≤ α ≤ 1/b²"),
          E("|F(P)|b² ≤ |PM|·|PN| ≤ |F(P)|a²"),
          P("最大值对应长轴方向，最小值对应短轴方向。整个过程不需要求出 M、N。", "CNBody")]

story += [PageBreak(), P("三、切线：二次方程出现重根", "CNH1"),
          P("直线与圆锥曲线相切时，两个交点合并为一个点，因此二次方程有二重根：", "CNBody"),
          E("t₁=t₂，　β²-4αγ=0"),
          P("所以判别式为零的几何意义就是：两个交点合并，直线变成切线。", "CNBody"),
          box("两相交点：两个不同实根；相切：一个二重根；没有实交点：没有实根。"),
          P("四、用参数给圆锥曲线上的点编号", "CNH1"),
          P("椭圆可用参数 t 表示为", "CNBody"),
          E("P(t)= ( a(1-t²)/(1+t²),  2bt/(1+t²) )"),
          P("用参数后，曲线上的点变成 t；复杂的几何条件就变成参数之间的代数关系。", "CNBody"),
          P("两点 P(t)、P(u) 的连线方程为", "CNBody"),
          E("(1-tu)x/a+(t+u)y/b=1+tu"),
          P("它只含有 t+u 与 tu。这正是韦达定理提供的两个量。", "CNBody"),
          P("两点连线的斜率为", "CNBody"),
          E("kᵗᵘ=(b/a)(tu-1)/(t+u)"),
          box("弦方程和斜率都依赖于 t+u、tu。遇到平行、垂直、斜率比等条件，应优先改写成这两个对称量。"),
          P("五、复杂斜率的韦达处理", "CNH1"),
          P("若 t₁、t₂ 是同一个二次方程的两个根，且某条线的斜率是", "CNBody"),
          E("k(t)=(αt+β)/(γt+δ)"),
          P("记 s=t₁+t₂，p=t₁t₂，则", "CNBody"),
          E("k(t₁)+k(t₂)=[2αγp+(αδ+βγ)s+2βδ]/[γ²p+γδs+δ²]"),
          E("k(t₁)k(t₂)=[α²p+αβs+β²]/[γ²p+γδs+δ²]"),
          P("这样只需知道 s、p，不必求出 t₁、t₂。", "CNBody")]

story += [PageBreak(), P("六、长度比：先平方，再化为参数式", "CNH1"),
          P("椭圆上两点 P(t)、P(u) 的距离平方为", "CNBody"),
          E("|P(t)P(u)|²=4(t-u)²[a²(t+u)²+b²(1-tu)²]/[(1+t²)²(1+u²)²]"),
          P("所以复杂长度比最好先平方。这样可以避免根号，并且很多部分仍然只含 t+u、tu。", "CNBody"),
          P("七、焦点与准线：用距离平方", "CNH1"),
          P("圆锥曲线的统一定义是", "CNBody"),
          E("PF/d(P,l)=e"),
          P("其中 F 是焦点，l 是准线，e 是离心率。计算时平方最方便：", "CNBody"),
          E("PF²=e²d(P,l)²"),
          P("因为点到焦点距离的平方、点到直线距离的平方都是二次式，代入参数后通常可以直接化简。", "CNBody"),
          P("例如椭圆 x²/a²+y²/b²=1 的右焦点为 F(c,0)，右准线为 x=a²/c，且 e=c/a。", "CNBody"),
          E("PF=e·d(P,l)"),
          P("遇到焦点、准线和线段比时，先把各个距离写成参数的函数，再比较它们的比值。", "CNBody"),
          P("八、渐近线：看二次项和无穷远方向", "CNH1"),
          P("设二次曲线为", "CNBody"),
          E("Ax²+Bxy+Cy²+Dx+Ey+F₀=0"),
          P("先求中心 (x₀,y₀)，再令 x=x₀+X，y=y₀+Y。渐近线方向只由二次项决定：", "CNBody"),
          E("AX²+BXY+CY²=0"),
          P("例如双曲线 x²/a²-y²/b²=1 的渐近线为", "CNBody"),
          E("y=±(b/a)x"),
          box("射影地说：椭圆没有实无穷远点；抛物线有一个二重无穷远点；双曲线有两个实无穷远点，因此双曲线有两条实渐近线。")]

story += [PageBreak(), P("九、调和关系：用交比而不是普通长度比", "CNH1"),
          P("若 A、B、C、D 在同一直线上，用有向坐标 a,b,c,d 表示，则交比为", "CNBody"),
          E("(A,B;C,D)=((c-a)/(c-b))·((d-b)/(d-a))"),
          P("调和关系就是", "CNBody"),
          E("(A,B;C,D)=-1"),
          P("等价地，使用有向线段可写成", "CNBody"),
          E("AC/BC=-AD/BD"),
          P("因此题目出现“两个线段比互为相反数”时，通常是在表达调和分割。", "CNBody"),
          P("十、极点极线：调和关系的来源", "CNH1"),
          P("设外点 P 向圆锥曲线引两条切线，切点为 A、B。任取过 P 的直线，交圆锥曲线于 M、N；若极线与 MN 交于 Q，则", "CNBody"),
          E("(M,N;P,Q)=-1"),
          P("所以遇到切点、极线、共线和调和关系时，应优先想到极点极线，而不是逐段计算。", "CNBody"),
          P("用齐次坐标表示圆锥曲线", "CNBody"),
          E("xᵀCx=0"),
          P("则点 p 的极线方程为", "CNBody"),
          E("xᵀCp=0"),
          P("高中阶段通常不必使用矩阵公式；把它理解为“极点决定一条特殊直线，且该直线产生调和关系”即可。", "CNBody"),
          P("十一、复杂构造的固定流程", "CNH1"),
          P("面对涉及不同点、不同直线、焦点、准线、渐近线和调和关系的综合题，可以按以下顺序处理：", "CNBody"),
          P("1. 给曲线上的点设参数 P(t)。", "CNBody"),
          P("2. 直线关系用行列式、弦方程或斜率表示。", "CNBody"),
          P("3. 长度关系用距离平方。", "CNBody"),
          P("4. 焦点准线关系用 PF²=e²d²。", "CNBody"),
          P("5. 渐近线只看中心和二次项。", "CNBody"),
          P("6. 调和关系用交比等于 -1。", "CNBody"),
          P("7. 消去多余参数，只保留参数的和与积。", "CNBody"),
          P("8. 最后用韦达定理、判别式或对称性收尾。", "CNBody")]

story += [PageBreak(), P("十二、统一记忆表", "CNH1")]
data = [
    [P("几何对象", "CNH2"), P("代数表达", "CNH2")],
    [P("两个交点", "CNBody"), E("αt²+βt+γ=0")],
    [P("交点参数的和、积", "CNBody"), E("t₁+t₂=-β/α， t₁t₂=γ/α")],
    [P("长度积", "CNBody"), E("|PM|·|PN|=|γ/α|")],
    [P("相切", "CNBody"), E("判别式=0，或 t₁=t₂")],
    [P("焦点准线", "CNBody"), E("PF²=e²d²")],
    [P("渐近线", "CNBody"), E("中心 + 二次项的零方向")],
    [P("调和关系", "CNBody"), E("(A,B;C,D)=-1")],
    [P("极线", "CNBody"), E("xᵀCp=0")],
]
tbl = Table(data, colWidths=[55*mm, 115*mm], repeatRows=1)
tbl.setStyle(TableStyle([
    ("BACKGROUND", (0,0), (-1,0), BLUE),
    ("TEXTCOLOR", (0,0), (-1,0), colors.white),
    ("GRID", (0,0), (-1,-1), 0.4, colors.HexColor("#B7C9E2")),
    ("VALIGN", (0,0), (-1,-1), "MIDDLE"),
    ("LEFTPADDING", (0,0), (-1,-1), 7),
    ("RIGHTPADDING", (0,0), (-1,-1), 7),
    ("TOPPADDING", (0,0), (-1,-1), 6),
    ("BOTTOMPADDING", (0,0), (-1,-1), 6),
    ("BACKGROUND", (0,1), (-1,-1), colors.HexColor("#F8FBFF")),
]))
story += [tbl, Spacer(1, 8), box("最后的判断：欧氏关系用距离平方，射影关系用交比，切线关系用双根，渐近关系看无穷远方向；具体计算尽量转化为参数的对称式。"),
          P("这套方法的目的不是增加公式，而是减少求点坐标的工作：先看关系属于哪一类，再选择对应的不变量。", "CNBody")]

doc = SimpleDocTemplate(OUT, pagesize=A4, rightMargin=20*mm, leftMargin=20*mm, topMargin=22*mm, bottomMargin=17*mm, title="圆锥曲线中的几何关系")
doc.build(story, onFirstPage=header_footer, onLaterPages=header_footer)
print(OUT)
