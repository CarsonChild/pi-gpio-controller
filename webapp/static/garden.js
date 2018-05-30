$(document).ready(function(){
    for(i=1;i<7;i++){
        checkboxes.push(new Checkbox(i));
    }
    $('#water').click(function(){
       water();
    });
});
var checkboxes = [];
function Checkbox(id){
    var _this = this;
    this.box=$("#valve"+id);
    this.chkd=true;
    this.box.css({"background-color": "#2C3C7B", "color":"#ffffff"});
    this.box.click(function(){
        _this.chkd = !_this.chkd;
        if(_this.chkd){
            _this.box.css({"background-color": "#2C3C7B", "color":"#ffffff"});
        } 
        else {
            _this.box.css({"background-color": "#ffffff","color":"#000000"});
        }
    });
}
function water(){
    var valves = "";
    for (i = 0; i<checkboxes.length; i++){
        if(checkboxes[i].chkd){
            valves += checkboxes[i].box.attr("pin-num");
        }
    } 
    $.get("/water/"+valves+"/"+$("#interval").val() );
}
