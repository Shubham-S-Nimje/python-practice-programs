{
 "cells": [
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "6f5516da",
   "metadata": {},
   "outputs": [
    {
     "name": "stdout",
     "output_type": "stream",
     "text": [
      "Server is Running\n"
     ]
    }
   ],
   "source": [
    "# Server Program\n",
    "import socket\n",
    "\n",
    "s=socket.socket()\n",
    "s.bind((\"localhost\",60))\n",
    "s.listen(5)\n",
    "print(\"Server is Running\")\n",
    "s.accept()\n",
    "print(\"Connection Established\")\n",
    "s.close()"
   ]
  },
  {
   "cell_type": "code",
   "execution_count": null,
   "id": "51e0951a",
   "metadata": {},
   "outputs": [],
   "source": [
    "# Client Program\n",
    "\n",
    "import socket\n",
    "s=socket.socket()\n",
    "s.connect((\"localhost\",60))\n",
    "s.close()"
   ]
  }
 ],
 "metadata": {
  "kernelspec": {
   "display_name": ".venv",
   "language": "python",
   "name": "python3"
  },
  "language_info": {
   "codemirror_mode": {
    "name": "ipython",
    "version": 3
   },
   "file_extension": ".py",
   "mimetype": "text/x-python",
   "name": "python",
   "nbconvert_exporter": "python",
   "pygments_lexer": "ipython3",
   "version": "3.13.1"
  }
 },
 "nbformat": 4,
 "nbformat_minor": 5
}
