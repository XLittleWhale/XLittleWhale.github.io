import Foundation
import CoreGraphics
import CoreText

let htmlPath = "/Users/cryowhale/Desktop/XLittleWhale.github.io/output/圆锥曲线几何关系讲义.html"
let pdfPath = "/Users/cryowhale/Desktop/XLittleWhale.github.io/output/圆锥曲线几何关系讲义.pdf"
let html = try String(contentsOfFile: htmlPath, encoding: .utf8)
let data = html.data(using: .utf8)!
let options: [NSAttributedString.DocumentReadingOptionKey: Any] = [
    .documentType: NSAttributedString.DocumentType.html,
    .characterEncoding: String.Encoding.utf8.rawValue
]
let source = try NSAttributedString(data: data, options: options, documentAttributes: nil)
let font = CTFontCreateWithName("STHeitiSC-Medium" as CFString, 10.5, nil)
let titleFont = CTFontCreateWithName("STHeitiSC-Medium" as CFString, 17, nil)
let mutable = NSMutableAttributedString(attributedString: source)
mutable.addAttribute(.font, value: font, range: NSRange(location: 0, length: mutable.length))

let page = CGRect(x: 0, y: 0, width: 595, height: 842)
let margin: CGFloat = 48
let textRect = CGRect(x: margin, y: 48, width: page.width - 2 * margin, height: page.height - 92)
var mediaBox = page
let context = CGContext(url: URL(fileURLWithPath: pdfPath) as CFURL, mediaBox: &mediaBox, nil)!
let framesetter = CTFramesetterCreateWithAttributedString(mutable as CFAttributedString)
var location = 0
var pageNo = 1
while location < mutable.length {
    context.beginPDFPage(nil)
    let path = CGPath(rect: textRect, transform: nil)
    let frame = CTFramesetterCreateFrame(framesetter, CFRange(location: location, length: 0), path, nil)
    context.saveGState()
    context.textMatrix = .identity
    context.translateBy(x: 0, y: page.height)
    context.scaleBy(x: 1, y: -1)
    CTFrameDraw(frame, context)
    context.restoreGState()
    context.setFillColor(gray: 0.45, alpha: 1)
    let footer = "圆锥曲线中几何关系的统一处理方法  ·  (pageNo)"
    let footerAttr = NSAttributedString(string: footer, attributes: [.font: CTFontCreateWithName("STHeitiSC-Medium" as CFString, 8, nil), .foregroundColor: CGColor(gray: 0.45, alpha: 1)])
    let footerLine = CTLineCreateWithAttributedString(footerAttr)
    context.saveGState()
    context.textMatrix = .identity
    context.translateBy(x: margin, y: 28)
    CTLineDraw(footerLine, context)
    context.restoreGState()
    context.endPDFPage()
    let visible = CTFrameGetVisibleStringRange(frame)
    if visible.length == 0 { break }
    location += visible.length
    pageNo += 1
}
context.closePDF()
print(pdfPath)
