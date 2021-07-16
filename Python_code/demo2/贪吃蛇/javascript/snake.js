/*
通过键盘输入，控制蛇的移动（上下左右和‘A’,‘D’）
每次判断蛇头是否在食物的位置，如果是，则蛇增长1个单位，重新放置食物
判断蛇头是否撞到‘墙壁’，如果是,则弹出提示结束游戏
*/

	//获取绘制工具
	/*
	var canvas = document.getElementById("canvas");
	var ctx = canvas.getContext("2d");//获取上下文
	ctx.moveTo(0,0);
	ctx.lineTo(450,450);*/
    //通过id获取元素
	var c=document.getElementById("canvas");
	//创建 context 对象
    //getContext("2d") 对象是内建的 HTML5 对象，拥有多种绘制路径、矩形、圆形、字符以及添加图像的方法。
    var ctx=c.getContext("2d");
    /*ctx.beginPath();
    ctx.moveTo(0,0);
    ctx.lineTo(450,450);
    ctx.stroke();
    */

    var snake =[];//定义一条蛇，画蛇的身体
    var snakeCount = 6;//初始化蛇的长度
	var foodx =0;//定义“食物”的横坐标
	var foody =0;//定义“食物”的纵坐标
    var togo =0;
    function drawtable()//画地图的函数
    {
    	for(var i=0;i<60;i++)//画竖线
    	{
    	    //设置颜色为黑色
    		ctx.strokeStyle="black";
    		//开始一条路径
    		ctx.beginPath();
    		//开始处
    		ctx.moveTo(15*i,0);
    		//结点处
    		ctx.lineTo(15*i,600);
    		//创建从当前点到开始点的路径
    		ctx.closePath();
    		//进行绘制
    		ctx.stroke();
    	}
        for(var j=0;j<40;j++)//画横线
    	{
    		ctx.strokeStyle="black";
    		ctx.beginPath();
    		ctx.moveTo(0,15*j);
    		ctx.lineTo(900,15*j);
    		ctx.closePath();
    		ctx.stroke();
    	}

    	for(var k=0;k<snakeCount;k++)//画蛇的身体
			{
			//设置或返回用于填充绘画的颜色
			ctx.fillStyle="#000";
			//设置蛇头颜色
			if (k==snakeCount-1)
			{
				ctx.fillStyle="red";//蛇头的颜色与身体区分开
			}
			ctx.fillRect(snake[k].x,snake[k].y,15,15);//前两个数是矩形的起始坐标，后两个数是矩形的长宽。

			}
			//绘制食物
    		ctx.fillStyle ="black";
	     ctx.fillRect(foodx,foody,15,15);
	     ctx.fill();

    }


    function start()//定义蛇的坐标
    {
    	//var snake =[];//定义一条蛇，画蛇的身体
        //var snakeCount = 6;//初始化蛇的长度

		for(var k=0;k<snakeCount;k++)
    		{
    			snake[k]={x:k*15,y:0};
            }

		  drawtable();
          addfood();//在start中调用添加食物函数

    }

    //在start中调用添加食物函数
    function addfood()
	{
	//随机定义食物位置
    //定义食物的横坐标
	foodx = Math.floor(Math.random()*60)*15; //随机产生一个0-1之间的数
    //定义食物纵坐标
	foody = Math.floor(Math.random()*40)*15;

		for (var k=0;k<snake;k++)
		{
		    //防止产生的随机食物落在蛇身上
			if (foodx==snake[k].x&&foody==sanke[k].y)
			{
			addfood();//重新添加食物
			}
		}


	}

   function move()
   {
	switch (togo)
	{
	case 1: snake.push({x:snake[snakeCount-1].x-15,y:snake[snakeCount-1].y}); break;//向左走
	case 2: snake.push({x:snake[snakeCount-1].x,y:snake[snakeCount-1].y-15}); break;//向上走
	case 3: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y}); break;//向右走
	case 4: snake.push({x:snake[snakeCount-1].x,y:snake[snakeCount-1].y+15}); break;//向下走
	case 5: snake.push({x:snake[snakeCount-1].x-15,y:snake[snakeCount-1].y-15}); break;//左上
	case 6: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y+15}); break;//右下
	default: snake.push({x:snake[snakeCount-1].x+15,y:snake[snakeCount-1].y});//默认向右走
	}
    snake.shift();//删除数组第一个元素
   	ctx.clearRect(0,0,900,600);//清除画布重新绘制
   	isEat();//判断是否吃到食物
	isDead();//判断是否死亡
	drawtable();
   }

   function keydown(e)
   {
   //捕获键盘上的输入，根据按键不同设置togo的值，为蛇的移动准备
   switch(e.keyCode)
		{
         case 37: togo=1; break;//左
		 case 38: togo=2; break;//上
		 case 39: togo=3; break;//右
		 case 40: togo=4; break;//下
		 case 65: togo=5; break;//A
		 case 68: togo=6; break;//D
		}
   }

   function isEat()//吃到食物后长度加1
   {
       if(snake[snakeCount-1].x==foodx&&snake[snakeCount-1].y==foody)
       {
           //重新添加食物
           addfood();
           //蛇长度+1
           snakeCount++;
           snake.unshift({x:-15,y:-15});
       }
   }

   function isDead()
   {
    //判断是否撞墙
    if (snake[snakeCount-1].x>885||snake[snakeCount-1].y>585||snake[snakeCount-1].x<0||snake[snakeCount-1].y<0)
		{
		//弹框提示
		alert("You are dead,GAME OVER!!!");
		window.location.reload();
		}
   }

   //添加监听事件，返回按键值
    document.onkeydown=function(e)
    {
    //获取按键值，为蛇的移动准备
	keydown(e);
    }

    //监听器，使javascript在页面加载完毕后开始执行
    window.onload = function()//调用函数
    {
        start();
        //每150ms调用一次move函数，即蛇不停地移动
        setInterval(move,150);
        drawtable();
    }

