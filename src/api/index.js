import { Router } from 'express';

let api = Router();

api.get('/', (req, res) => {
    res.json({
		test: '123'
	});
});

export default api;