import redis from 'redis';

const client = redis.createClient();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

function displaySchoolValue(schoolName) {
  client.get(schoolName, (error, replies) => {
    console.log(replies);
  });
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
