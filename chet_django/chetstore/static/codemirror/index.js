import '../node_modules/codemirror/lib/codemirror.js'
import '../node_modules/codemirror/mode/xml/xml.js';
window.onload = function(){
    
    let text = document.getElementById('pruebaCodeMirror')
    let editor = CodeMirror.fromTextArea(text, {            
        lineNumbers: true,
        mode: "xml"        
    });
    editor.setSize(null, "30%")
    editor.setOption("theme", "monokai")    
}