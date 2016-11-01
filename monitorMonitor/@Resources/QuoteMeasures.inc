[Rainmeter]
; DynamicWindowSize=1
; update = 5000
; OnUpdateAction = [!RainmeterSetVariable] Quote [QuoteMeasure]


[TennoText]
;FontColor=a5a5a5
; FontFace=Segoe UI
FontColor = 696969
FontFace = tenObet
FontSize=30
AntiAlias=1
StringStyle=Bold
; ClipString =0
; postfix = "                  "
; w = 1000

[DebugBacks]
x=0
y=0
h = 38
w = #SCREENAREAWIDTH#
solidcolor = 255,200,200, 0

; [QuoteMeasure]
; Measure=Plugin
; Plugin=QuotePlugin
; Pathname = "#@#/DualQuotes.txt"
; dynamicvariables = 1
; OnChangeAction = !SetVariable Quote [QuoteMeasure]


; [MeasureDown]
; Measure = String
; String = #Quote#
; RegExpSubstitute=1
; Substitute ="^[^,]+,": ""
; DynamicVariables = 1

; [MeasureUp]
; Measure = String
; String = #Quote#
; RegExpSubstitute=1
; Substitute =",.*": ""
; DynamicVariables = 1


[Variables]
Quoteu=dOnt drAh Tuh rAn mIh SotiN stwr
Quoted=ohwS ahohAh Tuh lEvz upOn Wr grAvz 