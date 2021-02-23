const dgram = require('dgram');
const sleep = require('sleep');
// 生成了一个udp服务
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
	console.log(`receive message from ${rinfo.address}:${rinfo.port}`);
	console.log(msg.toString());
	
});
//User i Wanna GET/POST HIS/INFO/
// 0x
client.send(`GET ROOM HIS`,9999,'192.168.0.183');
client.send(`GET ROOM INFO`,9999,'192.168.0.183');
client.send(`GET ROOM INFO`,9999,'192.168.0.183');
/*var times = 10;
while(times){
	sleep.sleep(1);
	
	times--;
}*/

