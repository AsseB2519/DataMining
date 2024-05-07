import { Injectable } from '@angular/core';
import Talk from 'talkjs';

@Injectable({
  providedIn: 'root'
})
export class TalkService {

  private currentUser: Talk.User | undefined;

  constructor() { }

  async createUser(applicationUser: any) {
    await Talk.ready;

    return new Talk.User({
      id: applicationUser.id,
      name: applicationUser.username,
      photoUrl: applicationUser.photoUrl
    });
  }

  async createCurrentSession() {
    
    await Talk.ready;
    const user = {
      id: 1,
      username: 'Me',
      photoUrl: 'https://www.shutterstock.com/image-vector/blank-avatar-photo-place-holder-600nw-1095249842.jpg',
      welcomeMessage: 'Hey there! How are you? :-)'
    };

    this.currentUser = await this.createUser(user);
    const session = new Talk.Session({
         appId: 'tuNjUD9D',
         me: this.currentUser
    });

    return session;
  }

  private async getOrCreateConversation(session: Talk.Session, otherApplicationUser: any) {
    if(!this.currentUser) return;

    const otherUser = await this.createUser(otherApplicationUser);
    const conversation = session.getOrCreateConversation(Talk.oneOnOneId(this.currentUser.id, otherUser));
    conversation.setParticipant(this.currentUser);
    conversation.setParticipant(otherUser);

    return conversation;
  }

  async createChatbox(session: Talk.Session) {
    const otherApplicationUser = {
      id: 2,
      username: 'LeisUM',
      photoUrl: 'https://t3.ftcdn.net/jpg/06/08/98/88/360_F_608988880_W8haNckegD4WOj9k4f9HAWsol0SxOURy.jpg',
      welcomeMessage: 'Hey, upload your pdf files.'
    };

    const conversation = await this.getOrCreateConversation(session, otherApplicationUser);
    const chatbox = session.createChatbox(conversation);

    return chatbox;
 }

}
