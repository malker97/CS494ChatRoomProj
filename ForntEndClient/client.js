const dgram = require('dgram');
const sleep = require('sleep');
const client = dgram.createSocket('udp4');
var host;
const readline = require('readline').createInterface({
  input: process.stdin,
  output: process.stdout
})
client.on('close',()=>{
	console.log('socket已关闭');
});

client.on('error',(err)=>{
	console.log(err);
});
client.on('message',(msg,rinfo)=>{
	if(msg=='exit') client.close();
	console.log(msg.toString());
	console.log(`receive message from ${rinfo.address}:${rinfo.port}`);
});
client.send(`这是来自客户端的内容`,9999,'192.168.0.183');
/*var times = 10;
while(times){
	sleep.sleep(1);
	
	times--;
}*/

