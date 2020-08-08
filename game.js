// var this.timer = setInterval(function foo(){};, 10000);
var timer = [];
function changeColor(){
	// if (type)
	timer.push(setInterval(randColor, 100));
}

function randColor(){
	code = '#' + addColorCode('');
	console.log(code);
	document.body.style.background = code;
}

function addColorCode(cur_code){
	var num = [0,1,2,3,4,5,6,7,8,9,'a','b','c','d','e','f'];
	one_code = num[Math.floor(Math.random()*16)];
	cur_code+=one_code;
	if (cur_code.length==6){
		return cur_code; 
	}
	else{
		return addColorCode(cur_code);
	}
}

let chg_btn = document.getElementById("change");
chg_btn.onclick = changeColor;

function stopChange(){
	for (var i = 0; i < timer.length; i++) {
		clearInterval(timer[i]);
	}
}

let stop_btn =  document.getElementById("stop");
stop_btn.onclick = stopChange;




