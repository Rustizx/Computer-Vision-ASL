import { MemoryRouter as Router, Routes, Route } from 'react-router-dom';
import VideoScreen from './screens/video-screen';
import './styles/App.scss';

export default function App() {
  return (
    <Router>
      <Routes>
        <Route path="/" element={<VideoScreen />} />
      </Routes>
    </Router>
  );
}
