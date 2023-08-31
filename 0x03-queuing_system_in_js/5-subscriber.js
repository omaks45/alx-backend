import redis from 'redis';
//import {promisify} from 'utils';

const subscriber = redis.createClient();

subscriber.on('error', (err) => {
  console.error(`Redis client not connected to the server: ${err}`);
});

subscriber.on('connect', () => console.log('Redis client connected to the server'));

subscriber.subscribe('holberton school channel');

subscriber.on('message', (channel, message) => {
  console.log(message);
  if (message === 'KILLER_SERVER') {
    subscriber.unscribe();
    subscriber.quit();
  }
});
