import redis from 'redis';
import {promisify} from 'util';

const client = redis.createClient();

client.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

client.on('connect', () => console.log('Redis client connected to the server'));

function setNewSchool(schoolName, value) {
  client.set(schoolName, value, redis.print);
}

async function displaySchoolValue(schoolName) {
  const getAsync = promisify(client.get).bind(client);
  try {
    const replies = await getAsync(schoolName);
    console.log(replies);
  } catch(error) {
      console.error(error);
  } finally {
      client.quit();
  }
}

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
